import streamlit as st
from vertexai.preview.language_models import ChatModel, ChatSession

import vertexai

def create_session():
    vertexai.init(project="amdanalysedocumentaire", location="us-central1")
    chat_model = ChatModel.from_pretrained("chat-bison")
    parameters = {
        "max_output_tokens": 8000,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40,
        "context":"""Vous etes un expert en finances publiques et politiques publiques. Vous assistez d\'autres consultants dans la rédaction d\'analyses documentaires et laa rédaction de rapports de missions"""
    }
    chat = ChatSession(model=chat_model, **parameters)
    return chat

def response(chat, message):
    response = chat.send_message(
        message=message, max_output_tokens=2040, temperature=0.2, top_k=40, top_p=0.8
    )
    return response.text

# Initialize the chat model
chat_model = create_session()

# Streamlit app
st.title("AMD INTERNATIONAL ASSISTANT OPERATIONNEL")

# User input
user_input = st.text_input("Vous: ")

if st.button("Envoyer"):
    # Get response from the chat model
    bot_response = response(chat_model, user_input)
    
    # Display the response
    st.text_area("IA AMD 1.0:", bot_response, height=500)

# Clear button
if st.button("Effacer"):
    st.text_area("IA AMD 1.0:", "")

# Note: This is a simple example and might need improvement based on your specific requirements.
