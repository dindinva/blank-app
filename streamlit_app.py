import streamlit as st
from google import genai


st.title("🎈 Gemini chat")
st.write("Gemini:คุยได้เลยนะ")
history=[]
client = genai.Client(api_key="AIzaSyD02r_b6nn1lzkEjA6dCewkDfNCgkY5IIY")

while True:
   ask=st.text_input("ฉัน:")
   history.append("ฉัน:"+ask)
   st.write("ฉัน:"+ask)
   response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=history,
)
   answer=response.text
   history.append("Gemini:"+answer)
   st.write("Gemini:"+answer)
   if len(history)>6:
      history.pop
      history.pop

