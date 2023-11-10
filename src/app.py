import gradio as gr
from vertexai.preview.language_models import ChatModel, InputOutputTextPair, ChatSession

import vertexai


def create_session():
    vertexai.init(project="amdanalysedocumentaire", location="us-central1")
    chat_model = ChatModel.from_pretrained("chat-bison")
    parameters = {
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
    }
    chat = chat_model.start_chat(
    context="""Vous etes un expert en finances publiques et politiques publiques. Vous assistez d\'autres consultants dans la rédaction d\'analyses documentaires et laa rédaction de rapports de missions""",
    )
    print(1)
    chat = ChatSession(model=chat_model, **parameters)
    print(2)
    return chat


def response(chat, message):
    response = chat.send_message(
        message=message, max_output_tokens=256, temperature=0.2, top_k=40, top_p=0.8
    )
    return response.text


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(
        [
            (
                "Bonjour, je suis l'Intelligence Artificielle AMD 1.0 . Je peux vous aider à rechercher des documents, analyser des documents et rédiger des rapports. Posez moi toutes vos questions.",
                None,
            )
        ],
        label="AMD INTERNATIONAL ASSISTANT OPERATIONNEL",
    ).style(height=400)
    msg = gr.Textbox()
    clear = gr.Button("Clear")
    chat_model = create_session()

    def respond(message, chat_history):
        texts = [message]
        print(message)
        bot_message = response(chat_model, message)
        print(bot_message)
        chat_history.append((message, bot_message))
        print(3)
        return "", chat_history
        print(4)

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    print(5)
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
