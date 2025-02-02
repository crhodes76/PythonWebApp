from flask import Flask, render_template, request, jsonify
from GeminiAiApiMethods import get_response
app = Flask(__name__, template_folder='views')

@app.route('/')
def home():
    return render_template('/Home/index.html')

@app.route('/gemini_query', methods=['POST'])
def gemini_query():
    print(request.data)
    data = request.get_json()
    print(data)
    text = data.get('question')
    response_text = get_response(text)
    return response_text

if __name__ == '__main__':
    app.run(debug=True)