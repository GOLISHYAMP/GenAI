from fastapi import FastAPI
from langchain_core.prompts.chat import ChatPromptTemplate
from langserve import add_routes
from langchain_ollama.chat_models import ChatOllama
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

qwen_model = ChatOllama(
    model = 'qwen2.5:1.5b',
    temperature=0.2
)

prompt1 = ChatPromptTemplate.from_template("Write an essay about {topic} with 100 words.")
add_routes( app, prompt1 | qwen_model, path = "/essay")

llama_model = ChatOllama(
    model = 'llama3.2:1b',
    temperature=0.2
)
prompt2 = ChatPromptTemplate.from_template("Write a poem about {topic} with 100 words.")

add_routes(app, prompt2 | llama_model, path="/poem")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)