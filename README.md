# resume-analyzer
📄 AI Resume Analyzer

This project analyzes resumes and matches them with job roles using Machine Learning.

## Features
- Upload resume (PDF)
- Extract text
- Job match percentage
- Suggestions for improvement

## Tech Stack
- Python
- Streamlit
- Scikit-learn

## How to Run
1. Install requirements
2. Run: streamlit run app.py

📌 Project Description

The AI Resume Analyzer is a machine learning-based application that analyzes resumes and matches them with suitable job roles. It extracts text from uploaded PDF resumes and compares it with predefined job descriptions to calculate a match score.

---

🎯 Objectives

- To analyze resume content automatically
- To match resumes with job roles
- To provide suggestions for improvement
- To demonstrate basic NLP and machine learning concepts

---

🚀 Features

- 📄 Upload Resume (PDF format)
- 🔍 Extract text from resume
- 📊 Calculate job match percentage
- 💡 Provide improvement suggestions
- 🖥️ Simple and interactive web interface

---

🧠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- PyPDF2

---

⚙️ How It Works

1. User uploads a resume in PDF format
2. Text is extracted using PyPDF2
3. Text is converted into numerical form using CountVectorizer
4. Cosine similarity is used to compare resume with job roles
5. Match percentage is displayed
6. Suggestions are generated based on missing skills

---

▶️ How to Run the Project

1. Install required libraries:
   
   pip install streamlit PyPDF2 scikit-learn

2. Run the application:
   
   streamlit run app.py

3. Open the browser and go to:
   
   http://localhost:8501

---

📊 Sample Job Roles

- Data Scientist
- Web Developer
- AI Engineer

---

💡 Future Improvements

- Add more job roles
- Use advanced NLP (spaCy)
- Improve UI design
- Add resume scoring system
- Deploy online

---

👨‍💻 Author

- LASYA SATTI

- LINK:-http://localhost:8501/

---

📌 Conclusion

This project demonstrates how machine learning and natural language processing can be used to analyze resumes and assist users in improving their job prospects.
