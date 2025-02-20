from flask import Flask, render_template, request, jsonify
from GeminiAiApiMethods import get_response, gemini_query_response
from models.MyTimeModel import MyTimeModel
from ChatGptMethods import chat_gpt_query_response
import logging
import requests

app = Flask(__name__, template_folder='views')

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return render_template('/Home/index.html')

@app.route('/my_time', methods=['GET', 'POST'])
def my_time():
    mytime_model = MyTimeModel()
    if request.method == 'POST':
        project_id = request.form['project_id']
        hours_worked = float(request.form['hours_worked'])
        date = request.form['date']
        work_type = request.form['work_type']
               
        # API POST request to /api/my_time_save
        try:
            response = requests.post(
                'http://127.0.0.1:5001/api/my_time_save',
                json={
                    'project_id': project_id,
                    'hours_worked': hours_worked,
                    'date': date,
                    'work_type': work_type
                }
            )
            response_data = response.json()
            mytime_model.project_id = response_data['data']['project_id']
            mytime_model.hours_worked = response_data['data']['hours_worked']
            mytime_model.date = response_data['data']['date']
            mytime_model.work_type = response_data['data']['work_type']
            mytime_model.records = response_data['all_records']
            logging.debug(f"API response: {response_data}")
        except Exception as e:
            logging.error(f"Error making API request: {e}")

    return render_template('/Home/my_time.html', mytime_model=mytime_model)

@app.route('/ai_query', methods=['POST'])
def ai_query():
    post_request = request.get_json()
    isChatGptRequest = post_request.get('theDataObject', {}).get('property_1')
    logging.debug(f"isChatGptRequest: {isChatGptRequest}")
    if isChatGptRequest is False:
        query_response = gemini_query_response(request.get_json())
        return query_response
    else:
        query_response = chat_gpt_query_response(request.get_json())
        return query_response

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        logging.error(f"Error running the Flask application: {e}")
        raise