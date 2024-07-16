import streamlit as st
st.title("Questions and Answer")
import google.generativeai as genai

# setting the api key
genai.configure(api_key="AIzaSyDqCyIG1wqwpDp1cB2M6whDrp0Z73qo5Ck")

# setting the text model
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

text_area= st.text_area("Enter Your Questions")

if st.button("Submit"):
    st.write("The answer of your questions is here")
    response= get_gemini_response(text_area)
    st.write(response)
























































