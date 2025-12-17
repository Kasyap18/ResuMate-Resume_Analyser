import streamlit as st
import PyPDF2
import os
import io
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="ResuMate", page_icon=":robot_face:", layout="centered")
st.title("ResuMate")
st.markdown("Your AI-powered resume assistant. Upload your resume and get instant feedback!")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Validate API key
if not GOOGLE_API_KEY:
    st.error("⚠️ **API Key Missing**: Please set the `GOOGLE_API_KEY` environment variable in your `.env` file.")
    st.info("Create a `.env` file in the project root with: `GOOGLE_API_KEY=your_api_key_here`")
    st.stop()

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are applying for: (optional)")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text
    
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

def generate_with_retry(client, prompt, models=["gemini-2.5-flash", "gemini-2.0-flash"], max_retries=3):
    """Generate content with retry logic and fallback models"""
    last_error = None
    
    for model in models:
        for attempt in range(max_retries):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                return response.text
            except Exception as e:
                last_error = e
                error_str = str(e)
                
                # Check if it's a retryable error (503, 429, or temporary issues)
                if "503" in error_str or "429" in error_str or "overloaded" in error_str.lower() or "unavailable" in error_str.lower():
                    if attempt < max_retries - 1:
                        wait_time = (2 ** attempt) + (time.time() % 1)  # Exponential backoff with jitter
                        time.sleep(wait_time)
                        continue
                    else:
                        # Try next model if retries exhausted
                        break
                elif "400" in error_str and "API key" in error_str:
                    # Invalid API key - don't retry, raise immediately
                    raise e
                else:
                    # Non-retryable error, raise immediately
                    raise e
    
    # If all models and retries failed, raise the last error
    raise last_error


if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("The uploaded file is empty or could not be read. Please upload a valid PDF or TXT file.")
            st.stop()
        
        prompt = f"""You are an expert career coach and resume reviewer.
        Please analyze this resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}
        
        Resume content:
        {file_content}
        Please provide your feedback in a clear and structured manner, it will play a crucial role in helping users improve their resumes.
        """

        with st.spinner("Analyzing your resume... This may take a moment."):
            client = genai.Client(api_key=GOOGLE_API_KEY)
            response_text = generate_with_retry(client, prompt)

        st.markdown("### Resume Analysis and Feedback")
        st.markdown(response_text)
    
    except Exception as e:
        st.error(f"An error occurred while processing the file: {str(e)}")