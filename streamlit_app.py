import streamlit as st
from google import genai


st.title("🎈 Gemini chat")
st.write("Gemini:คุยได้เลยนะ")
history=""
client = genai.Client(api_key="AIzaSyD02r_b6nn1lzkEjA6dCewkDfNCgkY5IIY")
ask=st.chat_input("ฉัน:")
if ask:
   history=history+ask+"\n"
   response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=history,
)
   answer=response.text
   history=history+answer+"\n"
   st.write(history)

