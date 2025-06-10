import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import pandas as pd
from pandasql import sqldf  # you can install this package via pip install pandasql
import matplotlib.pyplot as plt


def load_csv_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def execute_csv_query(sql_query, df):
    """
    Execute an SQL query on a DataFrame using pandasql.
    """
    return sqldf(sql_query, {"df": df}) 

def interpret_query(user_question, schema_info):
   # Load tokenizer and model
    model_name = "llmware/slim-sql-1b-v0"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Ensure device compatibility
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    prompt = {
    # "context" :  f"Given a database with tables {schema_info["TableName"]} ({schema_info["Columns"]})",
    "context" :  f"Given a database with tables df ({schema_info["Columns"]})",
    "query" : user_question
    }

    # Prepare prompt packaging used in fine-tuning process
    new_prompt = f"<human>: {prompt['context']} {prompt['query']}\n<bot>:"


    # Tokenize input
    inputs = tokenizer(new_prompt, return_tensors="pt").to(device)
    start_of_output = inputs.input_ids.shape[1]

    # Generate output
    outputs = model.generate(
        inputs.input_ids,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        temperature=0.3,
        max_new_tokens=100,
    )

    # Decode output
    output_only = tokenizer.decode(outputs[0][start_of_output:], skip_special_tokens=True)
    return output_only
    
def generate_chart(df, chart_type="bar", title="Chart"):
    """
    Generates and saves a chart from the DataFrame.
    """
    plt.figure(figsize=(8,6))
    
    if chart_type == "bar":
        df.plot(kind="bar")
    elif chart_type == "line":
        df.plot(kind="line")
    else:
        df.plot(kind="bar")
    
    plt.title(title)
    plt.tight_layout()
    chart_file = "chart.png"
    plt.savefig(chart_file)
    plt.close()
    return chart_file


def main():
    csv_file_path = "student_records.csv"
    df = load_csv_data(csv_file_path)
    schema_info = {"TableName" : csv_file_path.split('.')[0], "Columns": ', '.join(df.columns)}
    print("Welcome to the CSV Data Analysis Chatbot!")
    while True:
        user_question = input("\nEnter your question (or type 'exit' to quit): ")
        if user_question.lower() == "exit":
            break

        sql_query = interpret_query(user_question, schema_info)
        print(f"\nGenerated SQL Query:\n{sql_query}\n")
        try:
            execute = input("Proceed to execute the cmd on database [yes/no]").strip().lower()
            if execute == "yes":
                result_df = execute_csv_query(sql_query, df)
                print("Query Result:")
                print(result_df.head())
                graph = input("Proceed to execute the cmd on database [yes/no]").strip().lower()
                if graph == "yes":
                    chart_type = input("Enter chart type (bar/line): ").strip().lower()
                    chart_file = generate_chart(result_df, chart_type=chart_type, title="Query Chart")
                    print(f"Chart saved as {chart_file}")   
        except Exception as e:
            print(f"Error processing query: {e}")

if __name__ == "__main__":
    main()