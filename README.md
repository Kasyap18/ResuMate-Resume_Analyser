# 🤖 ResuMate — AI-Powered Resume Analyzer

ResuMate is an AI-powered resume analysis tool that helps job seekers improve their resumes with clear, actionable, and professional feedback.  
Simply upload your resume, optionally specify a target job role, and receive instant insights powered by Google Gemini.

---

## 🚀 Why ResuMate?

Many candidates struggle with unclear resume content, weak skill presentation, and ATS rejections.  
ResuMate solves this by acting as a **virtual career coach**, providing structured and constructive feedback tailored to your resume and job goals.

---

## ✨ Key Features

- 📄 Upload resumes in **PDF or TXT** format  
- 🎯 Job-role–specific feedback (optional input)  
- 🧠 AI-powered resume analysis using **Google Gemini**  
- 📌 Actionable suggestions on:
  - Content clarity & impact
  - Skills presentation
  - Experience descriptions
  - Resume improvements for better job alignment
- ⚡ Fast, simple, and user-friendly interface built with **Streamlit**

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI & web app)
- **Google Gemini API**
- **PyPDF2** (PDF text extraction)
- **dotenv** (environment variable management)

---

## 📂 Project Structure

ResuMate/
├── main.py # Streamlit application

├── README.md # Project documentation

├── .gitignore # Ignored files

├── pyproject.toml # Project configuration

├── uv.lock # Dependency lock file

└── .env # Environment variables (ignored in Git)



---

## ⚙️ Setup & Installation

1️⃣ Clone the repository

git clone https://github.com/Kasyap18/ResuMate-Resume_Analyser.git
cd ResuMate-Resume_Analyser

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Set up environment variables

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_gemini_api_key_here

▶️ Run the Application

streamlit run main.py


🧠 How It Works

User uploads a resume (PDF/TXT)

Resume text is extracted

A structured prompt is sent to Google Gemini

Gemini analyzes the resume as an expert career coach

Feedback is displayed in a clean, readable format

🔐 Security Note

The .env file is intentionally ignored to protect API keys.

Never commit your API keys to public repositories.

🌱 Future Enhancements

Resume scoring & ATS compatibility score

Skill gap analysis

Resume rewriting suggestions

Multiple job role comparisons

Downloadable feedback reports
