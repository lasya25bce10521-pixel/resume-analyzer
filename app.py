import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

job_roles = {
    "Data Scientist": "python machine learning data analysis statistics pandas numpy",
    "Web Developer": "html css javascript react node web development",
    "AI Engineer": "python deep learning neural networks tensorflow pytorch"
}

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and check job match!")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Resume Preview")
    st.write(resume_text[:500])

    st.subheader("Job Match Scores")

    for role, desc in job_roles.items():
        documents = [resume_text, desc]
        cv = CountVectorizer().fit_transform(documents)
        similarity = cosine_similarity(cv)[0][1]

        st.write(f"{role}: {round(similarity * 100, 2)} %")

    st.subheader("Suggestions")

    if "python" not in resume_text.lower():
        st.write("- Add Python skill")

    if "projects" not in resume_text.lower():
        st.write("- Add projects section")
        