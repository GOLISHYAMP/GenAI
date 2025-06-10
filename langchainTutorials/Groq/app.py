import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.tools.retriever import create_retriever_tool
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama.chat_models import ChatOllama
from langchain_chroma.vectorstores import Chroma
import os
import bs4
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# if 'vector' not in st.session_state:

