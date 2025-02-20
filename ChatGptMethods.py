import requests
from flask import Flask, render_template, request, jsonify
from datetime import datetime

def chat_gpt_query_response(data):
    API_KEY = ""
    theData = request.get_json()
    print(theData)
    text = theData.get('theDataObject', {}).get('ai_question')
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY
    },
    data = {
        "model": "gpt-3.5-turbo",
        "message":[{'role':'system', 'content': 'You are a helpful chatbot.'},
                   {'role': 'user', 'content': text}
        ]
    }
    response_data = requests.post("https://api.openapi.com/v1/chat/completions", headers=header, json=data)
    return response_data['choices'][0]['message']['content']    
