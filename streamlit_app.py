#gemini live chat
import asyncio
from google import genai
import streamlit as st

client = genai.Client(api_key="AIzaSyD02r_b6nn1lzkEjA6dCewkDfNCgkY5IIY", http_options={'api_version': 'v1alpha'})
model = "gemini-2.0-flash"

config = {"response_modalities": ["TEXT"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        while True:
            message = st.text_input("User> ")
            if message.lower() == "exit":
                break
            await session.send(input=message, end_of_turn=True)

            async for response in session.receive():
                if response.text is not None:
                    answer=response.text
                    
                    st.write(answer)
asyncio.run(main())
