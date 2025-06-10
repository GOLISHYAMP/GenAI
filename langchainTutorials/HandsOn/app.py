from langchain_ollama.chat_models import ChatOllama 
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts.chat import ChatPromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(
    model = "qwen2.5:1.5b",
    temperature = 0.5)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Assistant, who gives answer to asked questions"),
    ("human", "{message}"),
])

outputParser = StrOutputParser()

chain = prompt | llm | outputParser

st.title("Here is your Chatbot")
given_input = st.text_input(label="Ask me any question")

if given_input:
    result=chain.invoke({'message': given_input})
    st.write(result)