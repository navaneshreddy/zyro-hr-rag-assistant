import streamlit as st

st.set_page_config(
    page_title="Zyro Dynamics HR Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Zyro Dynamics HR Assistant")
st.write("Ask questions about Zyro Dynamics HR policies.")

question = st.text_input("Enter your HR question:")

if question:
    st.info("This is the deployed demo app for the Zyro Dynamics HR Assistant.")
    st.write("Question:", question)
    st.write("Answer: Please refer to the Kaggle notebook for the full RAG-powered response.")