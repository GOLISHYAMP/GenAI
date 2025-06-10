import requests
import streamlit as st

def get_qwen_response(input):
    response = requests.post("http://localhost:8000/essay/invoke",
                            json={"input": {"topic": input}})
    return response.json()['output']['content']

def get_llama_response(input):
    response = requests.post("http://localhost:8000/poem/invoke",
                            json={"input": {"topic": input}})
    return response.json()['output']['content']

st.title("Langchain Demo with Qwen and llama")
essay_input = st.text_input("Write an essay on")
poem_input = st.text_input("Write a poem on")

if essay_input:
    st.write(get_qwen_response(essay_input))
if poem_input:
    st.write(get_llama_response(poem_input))