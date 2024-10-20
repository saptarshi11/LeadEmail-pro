# 📧 LeadEmail Pro
LeadEmail Pro for services company using groq, langchain and streamlit. It allows users to input the URL of a company's careers page. The tool then extracts job listings from that page and generates personalized cold emails. These emails include relevant portfolio links sourced from a vector database, based on the specific job descriptions. 

**Imagine a scenario:**

- Nike needs a Principal Software Engineer and is spending time and resources in the hiring process, on boarding, training etc
- Atlit is Software Development company can provide a dedicated software development engineer to Nike. So, the business development executive (Saptarshi) from Atlit is going to reach out to Nike via a cold email.

![Screenshot 2024-10-20 214734](https://github.com/user-attachments/assets/ef271ecb-420a-423e-bcd4-20249dc384f2)

## Architecture Diagram


![Screenshot 2024-10-20 220420](https://github.com/user-attachments/assets/7b9cb7f1-3f51-4579-9b19-b0a9ede0a484)

## Set-up
1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 


2. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   streamlit run app/main.py
   ```
   

