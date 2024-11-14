Installed required libraries like mysql-connector-python, os, python-dotenv, transformers-4.35.2, torch, accelerate
mysql-connector-python - to connect to database server.
os - to access environmental variables.
python-dotenv - to load environmental variables to the main script.
transformers - used to access pre-trained models for various nlp tasks.
torch - provides wide range of funtionalities for scientific computing and deep learning.
accelerate - used to optimize model loading with low cpu and low memory usage which in turn makes the model loading faster.


databasebot.py
- Imported mysql-connector-python, os, python-dotenv
- Loaded env vars.
- Established a connection to database server.
- Defined execute_query function which will take the query as input, execute the query and returns the results.


.env
- Used to store the confidential details like database name, database user, password, host name.


natural_sql_7b.py
- Imported transformers-4.35.2, torch, accelerate
- Created an object for accelerator
- Tokenizers are essential tools in machine learning, especially in natural language processing (NLP). They break down text into smaller units called tokens. Tokenization makes it easier for computers to understand and process the text. It’s used for tasks like translation, sentiment analysis, and all of NLP.
- AutoTokenizer is a special class in the Huggingface Transformers library. It helps you choose the right tokenizer for your model without knowing the details. Think of it as a smart assistant that knows which tool to use for the job. The AutoTokenizer is easy to use. You don’t have to remember which tokenizer goes with which model. It ensures you use the correct tokenizer for the model, reducing errors and improving consistency. Autotokenizer is flexible. It works with many different models, allowing you to switch models without changing much code.
- AutoModelForCausalLM - This module allows us to load a pre-trained causal language model. Causal language models can generate text based on a given prompt or context.
- Loaded pre trained tokenizer and model.
- Model and data preparation for distributed training is completely handled by the Accelerator object and its Accelerator.prepare() method
- Defined generate_sql_query funtion - passed prompt as parameter.
- Tokenize the input prompt and return tensor to inputs variable.
- Generate the output(sql query) with generate() and pass max_length and temperature.
- Decode the tokenizer and return sql query.
- Finally in the main function, pass the prompt(text from which sql query should be generated and executed.)
- Call generate_sql_query and pass the generated sql query to execute query funtion.


chatbot.py
- Defined a basic route for rendering the chatbot HTML page and an endpoint for handling chatbot messages.


templates/chatbot_ui.html
- HTML, CSS and Javascript to create chatbot UI.