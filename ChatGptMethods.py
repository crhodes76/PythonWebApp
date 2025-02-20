import requests
from flask import request

def chat_gpt_query_response(data):
    API_KEY = ""
    theData = request.get_json()
    text = theData.get('theDataObject', {}).get('ai_question')
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {'role': 'system', 'content': 'You are a helpful chatbot.'},
            {'role': 'user', 'content': text}
        ]
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    response_data = response.json()
    return response_data['choices'][0]['message']['content']