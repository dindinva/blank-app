from google import genai
import streamlit as st

st.title("Gemini-like chatbot")

client = genai.Client(api_key="AIzaSyD02r_b6nn1lzkEjA6dCewkDfNCgkY5IIY")
history=""
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"]=="user":history=history+message["content"]

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    prompt=history+prompt

    with st.chat_message("assistant"):
        stream = client.models.generate_content(model="gemini-2.0-flash",contents=prompt)
        response=stream.text
        st.write(response)
        history=""
    st.session_state.messages.append({"role": "assistant", "content": response})
    
