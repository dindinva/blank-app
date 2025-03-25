import streamlit as st
from google import genai


st.title("🎈 Gemini chat")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
client = genai.Client(api_key="AIzaSyD02r_b6nn1lzkEjA6dCewkDfNCgkY5IIY")
ask=st.chat_input("Ask me..."," ")
if ask:
   response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=ask,
)

   st.write(response.text)

