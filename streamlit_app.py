import streamlit as st
from google import genai

history=[]
st.title("🎈 Gemini chat")
st.write("Gemini:คุยได้เลยนะ")
client = genai.Client(api_key="AIzaSyD02r_b6nn1lzkEjA6dCewkDfNCgkY5IIY")
ask=st.text_input("ฉัน")
st.button("ส่ง",on_click=gen)
def gen():
   
   history.append("ฉัน:"+ask)
   st.write("ฉัน:"+ask)
   response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=history,
)
   answer=response.text
   history.append("Gemini:"+answer)
   st.write("Gemini:"+answer)
   #st.write(history)
   if len(history)>7:
      history.pop
      history.pop


