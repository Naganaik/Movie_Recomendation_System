import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

# MOvie Recomendation System
st.title("🍿🎥✮⋆Movie Recomendation System 🍿🎥✮⋆ ")

user_input=st.text_input("Enter the Movie Name")
submit=st.button("Click here.....")

if submit and user_input.strip():
    st.markdown('Movie name has been entered')
else:
    st.warning('Enter the movie name')
    





    
model=genai.GenerativeModel("gemini-2.5-flash-lite")
if submit and user_input.strip():
    st.markdown(f'movie name entered: {user_input}')
    response=model.generate_content(f'Generate movie recomendation related to : {user_input}')
    st.write(f'Related recomendation for similar movies:\n {response.text}')
else:
    st.write('You need to enter the movie name')
    
if submit:
    st.markdown('This is created by ❤️ Ayush')
else:
    pass
    
    
    
