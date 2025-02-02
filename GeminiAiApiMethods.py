
import google.generativeai as genai

def get_response(user_input):
        API_KEY = "AIzaSyAX6aOzupGfAW8njCjBPo6DQt6FitNr6cg"
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)  # Ensure correct method call
        return response.text 
    

