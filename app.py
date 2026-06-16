import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import AzureChatOpenAI

import credentials
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

#  Key Vault
credential = DefaultAzureCredential()
kv_uri = credentials.credential.KV_URI
secret_client = SecretClient(vault_url=kv_uri, credential=credential)
secret = secret_client.get_secret(credentials.credential.SECRET_KEY)

# LangChain Chat Model
chat = AzureChatOpenAI(
    azure_endpoint=credentials.credential.ENDPOINT,
    api_key=secret.value,
    deployment_name="gpt-4o",
    api_version=credentials.credential.API_VERSION,
    temperature=0.5
)

# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant")
    ]


def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))

    answer = chat.invoke(st.session_state['flowmessages'])

    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content


user_input = st.text_input("Input: ")

if st.button("Ask the question"):
    response = get_chatmodel_response(user_input)
    st.subheader("The Response is")
    st.write(response)
