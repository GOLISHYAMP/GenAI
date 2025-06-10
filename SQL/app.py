# from fastapi import FastAPI
# import openai
# # import mysql.connector  # or use psycopg2 for PostgreSQL

# app = FastAPI()

# # Set your OpenAI API key
# OPENAI_API_KEY = ""

# def text_to_sql(nl_query):
#     """Convert natural language to SQL using OpenAI GPT-4."""
#     response = openai.ChatCompletion.create(
#         model="gpt-4-turbo",
#         messages=[{"role": "system", "content": "You are an SQL expert."},
#                   {"role": "user", "content": f"Convert this to SQL: {nl_query}"}],
#         api_key=OPENAI_API_KEY
#     )
#     sql_query = response["choices"][0]["message"]["content"]
#     return sql_query

# # def execute_sql(sql_query):
# #     """Execute SQL query on Docker-hosted database."""
# #     conn = mysql.connector.connect(
# #         host="localhost",
# #         user="user",
# #         password="password",
# #         database="mydatabase",
# #         port=3306  # Change to 5432 for PostgreSQL
# #     )
# #     cursor = conn.cursor()
# #     cursor.execute(sql_query)
# #     results = cursor.fetchall()
# #     conn.close()
# #     return results

# @app.get("/query")
# def get_data(nl_query: str):
#     """Receive natural language query, generate SQL, execute it, and return results."""
#     sql_query = text_to_sql(nl_query)
#     # results = execute_sql(sql_query)
#     # return {"query": sql_query, "results": results}
#     return {"query": sql_query}

#Hugging face


from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


# model_name = "Salesforce/grappa_large"  # If you want to try this again
# tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=HF_TOKEN)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name, use_auth_token=HF_TOKEN)
# Load model directly
from transformers import AutoModel
model = AutoModel.from_pretrained("jossthebos/fine_tuned_ollama_nl2sqlV2")

def text_to_sql(nl_query):
    """Convert natural language to SQL using Hugging Face model."""
    inputs = tokenizer(nl_query, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs)
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query

from fastapi import FastAPI
# import mysql.connector  # Use psycopg2 for PostgreSQL

app = FastAPI()

# def execute_sql(sql_query):
#     """Execute SQL query on local MySQL database."""
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="your_user",
#         password="your_password",
#         database="your_database"
#     )
#     cursor = conn.cursor()
#     cursor.execute(sql_query)
#     results = cursor.fetchall()
#     conn.close()
#     return results

@app.get("/query")
def get_data(nl_query: str):
    """Convert NL to SQL, execute it, and return results."""
    sql_query = text_to_sql(nl_query)
    # results = execute_sql(sql_query)
    return {"query": sql_query}
