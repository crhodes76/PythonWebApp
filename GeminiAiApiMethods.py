
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from datetime import datetime


def gemini_query_response(data):
    theData = request.get_json()
    print(theData)
    text = theData.get('theDataObject', {}).get('ai_question')
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
    

def get_response(user_input):
        API_KEY = ""
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)  # Ensure correct method call
        return response.text 