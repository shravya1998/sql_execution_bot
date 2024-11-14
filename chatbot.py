from flask import Flask, request, jsonify
from databasebot import execute_query
from base_text_to_sql_small import translate_to_sql_select
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('chatbot_ui.html')

@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Get user input from JSON request
    user_input = request.json.get("query", "")
    
    # Generate SQL query from user input
    sql_query = translate_to_sql_select(user_input)
    print("Generated SQL Query:", sql_query)

    # Execute SQL query and get results
    try:
        results = execute_query(sql_query)
        response = {"query": sql_query, "results": results}
    except Exception as e:
        response = {"error": str(e)}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')