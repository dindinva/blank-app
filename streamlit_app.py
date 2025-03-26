import streamlit as st
from google import genai


st.title("🎈 Gemini chat")
st.write("Gemini:คุยได้เลยนะ")
client = genai.Client(api_key="AIzaSyD02r_b6nn1lzkEjA6dCewkDfNCgkY5IIY")
ask=st.text_input("ฉัน:")
if ask:
 
   response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=ask,
)

   st.write(response.text)

   

