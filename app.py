import os
import streamlit as st
from dotenv import load_dotenv
from mistralai.client import Mistral

# Load environment variables from .env file
load_dotenv()

# Initialize the Mistral Client
# It automatically picks up MISTRAL_API_KEY from the environment
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    st.error("Missing MISTRAL_API_KEY. Please set it in your .env file.")
    st.stop()

client = Mistral(api_key=api_key)

# Configure the Streamlit page layout
st.set_page_config(page_title="Mistral AI Assistant", page_icon="🤖")
st.title("Mistral AI Web Assistant")

# Choose a cost-effective, high-performing model (e.g., mistral-medium-latest)
# Alternative models include: "mistral-large-latest" or "open-mistral-7b"
MODEL_NAME = "mistral-medium-latest"

# Maintain chat history using Streamlit's session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages from history on application rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capture new user input from the chat interface
if user_prompt := st.chat_input("How can I help you today?"):
    
    # Render and store user message
    with st.chat_message("user"):
        st.markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Prepare streaming response container for the assistant
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Query Mistral API with streaming enabled
            # mapping current history format directly into the API call
            stream_response = client.chat.stream(
                model=MODEL_NAME,
                messages=st.session_state.messages
            )
            
            # Consume chunks from the stream in real-time
            for chunk in stream_response:
                chunk_text = chunk.data.choices[0].delta.content
                if chunk_text:
                    full_response += chunk_text
                    response_placeholder.markdown(full_response + "▌")
            
            # Display final polished message without the cursor
            response_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            full_response = "Sorry, I encountered an error processing that request."
            response_placeholder.markdown(full_response)

    # Save assistant response to session state history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
