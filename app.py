import streamlit as st

# Basic Configuration
st.set_page_config(page_title="Jaswanth Tiruveedhula Portfolio", layout="wide")

# Header
st.title("Jaswanth Tiruveedhula")
st.subheader("Transforming Data into Insights | Machine Learning Enthusiast")
st.write("[LinkedIn](https://www.linkedin.com/in/jaswanth-tiruveedhula) | [GitHub](https://github.com/jaswanth-tiruvee) | [Resume](#)")

# About Me Section
st.header("About Me")
st.write("""
I'm a Data Science graduate student with expertise in Machine Learning, Cloud Computing, and Data Analysis. 
I have hands-on experience in building scalable solutions and a passion for leveraging emerging technologies.
""")

# Skills
st.header("Skills")
st.write("""
- **Programming Languages**: Python, Java, R, C
- **Machine Learning**: TensorFlow, Scikit-learn, NLP
- **Tools**: Jupyter Notebook, Streamlit, SQL
- **Cloud**: Azure, Terraform, PowerShell
""")

# Projects Section
st.header("Projects")
projects = [
    {"title": "Speech Emotion Recognition", 
     "description": "Emotion classification using audio signals with MFCC and Mel-Spectrogram analysis.", 
     "link": "https://github.com/jaswanth-tiruvee/Speech_Emotion_Recognition_using-MFCC-and-mel-spectrogram"},
    {"title": "AI-Based Waste Sorting Machine", 
     "description": "Automated waste classification using machine learning for enhanced recycling.", 
     "link": "https://github.com/jaswanth-tiruvee/AI-Based_Waste-Sorting-Machine"},
    {"title": "Loan Prediction Application", 
     "description": "Predicting loan eligibility using ML models with a Streamlit interface.", 
     "link": "https://github.com/jaswanth-tiruvee/Loan_Prediction_Application-Streamlit-Hosting"},
    {"title": "Database Normalization for Instacart", 
     "description": "Optimized database performance through normalization techniques.", 
     "link": "https://github.com/jaswanth-tiruvee/Instacart--DB-Normalization"}
]

for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
    st.write(f"[GitHub Repository]({project['link']})")

# Contact Section
st.header("Contact Me")
st.write("Feel free to reach out through [LinkedIn](https://www.linkedin.com/in/jaswanth-tiruveedhula) or email at jaswanthtiruveedhula@gmail.com.")
