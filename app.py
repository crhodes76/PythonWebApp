from flask import Flask, render_template, request, jsonify
from GeminiAiApiMethods import get_response
from datetime import datetime
app = Flask(__name__, template_folder='views')

@app.route('/')
def home():
    return render_template('/Home/index.html')

@app.route('/gemini_query', methods=['POST'])

def gemini_query():
    data = request.get_json()
    print(data)
    text = data.get('dataObject', {}).get('question')
    response_text = get_response(text)
    response_data = {
        "status": "success",
        "message": "gemini response object",
        "dateTime": datetime.now().strftime("%m/%d/%Y %H:%M:%S"),
        "data": {
            "key1": response_text.replace('*', ''),
        }
    }
    return response_data

if __name__ == '__main__':
    app.run(debug=True)