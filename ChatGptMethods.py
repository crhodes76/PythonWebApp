import requests
from flask import request

def chat_gpt_query_response(data):
    API_KEY = "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"
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