# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from accelerate import Accelerator
from databasebot import execute_query
accelerator = Accelerator()
tokenizer = AutoTokenizer.from_pretrained("suriya7/t5-base-text-to-sql")
model = AutoModelForSeq2SeqLM.from_pretrained("suriya7/t5-base-text-to-sql")
model = accelerator.prepare(model)

def translate_to_sql_select(english_query):
  input_text = ("translate English to SQL: ", english_query)
  input_ids = tokenizer.encode(input_text, return_tensors="pt")
  outputs = model.generate(input_ids)
  sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
  return sql_query

# Example usage
if __name__ == '__main__':
    english_query = "Find the details of first five employees whose first name starts with A."
    sql_query = translate_to_sql_select(english_query)
    print("SQL Query:", sql_query)

    # Execute the query and fetch results
    results = execute_query(sql_query)
    for row in results:
        print(row)
