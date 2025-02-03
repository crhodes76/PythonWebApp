from flask import Flask, render_template, request, jsonify
from GeminiAiApiMethods import get_response, gemini_query_response
from datetime import datetime
app = Flask(__name__, template_folder='views')

@app.route('/')
def home():
    return render_template('/Home/index.html')

@app.route('/gemini_query', methods=['POST'])

def gemini_query():
    query_response = gemini_query_response(request.get_json())
    return query_response

if __name__ == '__main__':
    app.run(debug=True)