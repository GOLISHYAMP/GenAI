# from langchain_ollama.chat_models import ChatOllama 
# from langchain_core.output_parsers.string import StrOutputParser
# from langchain_core.prompts.chat import ChatPromptTemplate
# import streamlit as st
# import os
# from dotenv import load_dotenv
# load_dotenv()

# from langchain_huggingface import ChatHuggingFace

# # llm = HuggingFaceEndpoint(
# #     repo_id="microsoft/Phi-3-mini-4k-instruct",
# #     task="text-generation",
# #     max_new_tokens=512,
# #     do_sample=False,
# #     repetition_penalty=1.03,
# # )
# llm = 

# chat = ChatHuggingFace(llm=llm, verbose=True)


# # llm = ChatOllama(
# #     model = "qwen2.5:1.5b",
# #     temperature = 0.5)

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful Assistant, who gives answer to asked questions"),
#     ("human", "{message}"),
# ])

# outputParser = StrOutputParser()

# chain = prompt | llm | outputParser

# st.title("Here is your Chatbot")
# given_input = st.text_input(label="Ask me any question")

# if given_input:
#     result=chain.invoke({'message': given_input})
#     st.write(result)
#######################################################################################
from langchain_huggingface import HuggingFacePipeline
# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# model_id = "Qwen/Qwen2.5-1.5B-Instruct"
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(model_id)
# pipe = pipeline(
#     "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10
# )
# hf = HuggingFacePipeline(pipeline=pipe)
########################################################################################

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

model_id = "Qwen/Qwen2.5-1.5B-Instruct"

model = AutoModelForCausalLM.from_pretrained(model_id, load_in_4bit = True, device_map = 'auto', torch_dtype = torch.float16)

tokenizer = AutoTokenizer.from_pretrained(model_id)

pipe  = pipeline("text-generation", model=model, tokenizer=tokenizer)
hf = HuggingFacePipeline(pipeline=pipe)

print(hf.invoke("tell me about India"))
