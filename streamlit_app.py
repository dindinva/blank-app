from google import genai
import streamlit as st

st.title("Gemini-like clone")

client = genai.Client(api_key="AIzaSyD02r_b6nn1lzkEjA6dCewkDfNCgkY5IIY")

if "genai_model" not in st.session_state:
    st.session_state["genai_model"] = "gemini-2.0-flash"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.models.generate_content(
            model=st.session_state["genai_model"],
            contents=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
