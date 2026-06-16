# 📘 Conversational Q&A Chatbot (Azure OpenAI + Streamlit)

## 🚀 Overview

This project is a Conversational Q&A Chatbot built using:

- Streamlit for UI
- LangChain for conversation handling
- Azure OpenAI (GPT-4o) for responses
- Azure Key Vault for secure API key management

The chatbot maintains conversation history and provides contextual responses.

---

## 🧠 Features

- Conversational chat with memory
- Azure OpenAI (GPT-4o) integration
- Secure API key via Azure Key Vault
- Interactive Streamlit UI
- Stateful chat history

---

## 📦 Installation

pip install streamlit langchain langchain-core langchain-openai azure-identity azure-keyvault-secrets

---

## ⚙️ Configuration

Update credentials.py:

class credential:
    KV_URI = "https://<your-keyvault>.vault.azure.net/"
    SECRET_KEY = "<your-secret>"
    ENDPOINT = "https://<your-openai>.openai.azure.com/"
    API_VERSION = "2024-02-15-preview"

---

## ▶️ Run

streamlit run app.py

---

## 💬 Usage

1. Enter your query
2. Click 'Ask the question'
3. View chatbot response

---

## 📂 Project Structure

AI_Engineer/
│
├── app.py
├── credentials.py
└── README.md

---

## 🔧 Tech Stack

- Streamlit
- LangChain
- Azure OpenAI
- Azure Key Vault

---

## 👨‍💻 Author

Karthik Prakash Hudedamani

