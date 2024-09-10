from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load all the environment variables from .env
load_dotenv()

# Configure genAI API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load Gemini Pro Vision
model=genai.GenerativeModel('gemini-1.5-flash')

# Configure streamlit app
st.header("Chat with Gemini")

# Start chat session
chat_session = model.start_chat()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Get gemini response
    response_gemini = chat_session.send_message(prompt).text
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.write(response_gemini)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_gemini})