import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from accelerate import Accelerator
from databasebot import execute_query


accelerator = Accelerator()
tokenizer = AutoTokenizer.from_pretrained("chatdb/natural-sql-7b")
model = AutoModelForCausalLM.from_pretrained(
    "chatdb/natural-sql-7b",
    device_map="auto",
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True
)
model = accelerator.prepare(model)


def generate_sql_query(prompt):
    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
    
    # Generate SQL output with the model
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100, temperature=0.5)
    
    # Decode the generated output to get the SQL query
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query


if __name__ == '__main__':
    # Task 
    prompt = "Find the details of employees whose first name starts with A."

    # Generate SQL query
    sql_query = generate_sql_query(prompt)
    print("Generated SQL Query:", sql_query)

    # Execute the query and fetch results
    results = execute_query(sql_query)
    for row in results:
        print(row)