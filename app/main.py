import streamlit as st
from langchain.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
import logging

# Setup logging
logging.basicConfig(level=logging.ERROR)

def create_streamlit_app(llm: Chain, portfolio: Portfolio, clean_text: callable) -> None:
    st.title("📧 LeadEmail Pro")
    
    # Input URL
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
    submit_button = st.button("Submit")
    
    if submit_button:
        with st.spinner('Processing...'):
            try:
                # Load data from the web page
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                
                # Cache portfolio to avoid repeated loads
                if 'portfolio_loaded' not in st.session_state:
                    portfolio.load_portfolio()
                    st.session_state['portfolio_loaded'] = True

                # Extract jobs and generate emails
                jobs = llm.extract_jobs(data)
                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)
                    st.code(email, language='markdown')
            
            # More specific error handling
            except ConnectionError:
                st.error("Network issue: Unable to fetch data from the URL.")
            except ValueError as e:
                st.error(f"Parsing error: {e}")
            except Exception as e:
                logging.error(f"Unexpected error: {e}", exc_info=True)
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Initialize the chain and portfolio
    chain = Chain()
    portfolio = Portfolio()

    # Streamlit page config
    st.set_page_config(layout="wide", page_title="LeadEmail Pro", page_icon="📧")
    
    # Run the app
    create_streamlit_app(chain, portfolio, clean_text)


