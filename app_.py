import streamlit as st
from vertexai.preview.language_models import ChatModel, ChatSession
import os

import vertexai

from google.cloud import aiplatform
import streamlit.components.v1 as components

# Your existing Streamlit app content goes here

# Add a blue sidebar with instructions
st.markdown(
    """
    <style>
        .sidebar {
            background-color: #3498db;  /* Blue color */
            padding: 20px;
            color: #fff;  /* White text */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Instructions in the blue sidebar
st.sidebar.title("Instructions")
st.sidebar.write("Bonjour cher Agent de AMD, je suis ravi de vous revoir.")
st.sidebar.write("Je suis l'assistant opérationnel de AMD International, et je peux vous aider à effectuer les taches suivantes:")
st.sidebar.write("Effectuer une analyse d'un document spécifique, effectuer une analyse d'un concept et d'une entité liée aux finances pupliques,politiques publiques, ou tout autre domaine d'activités de AMD International.")
st.sidebar.write("Je peux également vous aider à rédiger vos rapports et analyses qualitatives, pourvu que les documents contenant les informations requises fassent partie du gestionnaire de documents.")
st.sidebar.write("Afin de me permettre de mieux vous appuyer dans l'exécution de vos taches, assurez vous de me fournir les documents nécessaires et à jour dans le gestionnaire de documents.")
st.sidebar.write("En cas de difficultés, veuillez contacter le Service des Systèmes d'Informations, Data et Intelligence Artificielle de AMD International au +226 25 46 55 02.")
key_path = st.secrets["account_key"]

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project='amdanalysedocumentaire',

    # the Vertex AI region you will use
    # defaults to us-central1
    location='us-central1',

    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://amddoc',


)

st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)


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
