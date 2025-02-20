import logging
import requests

def my_time_save(request):
    try:
        response = requests.post(
            'http://127.0.0.1:5001/api/my_time_save',
            json={
                'project_id': request.form['project_id'],
                'hours_worked': request.form['hours_worked'],
                'date': request.form['date'],
                'work_type': request.form['work_type'],
            }
        )
        response_data = response.json()
        return response_data
        logging.debug(f"API response: {response_data}")
    except Exception as e:
        logging.error(f"Error making API request: {e}")
        
        
def fetch_all_records(userid: str):
    # API GET request to /api/my_time
    # API POST request to /api/my_time_save
    try:
        response = requests.get(
            'http://127.0.0.1:5001/api/get_records_by_userid',
            json={
                'userid': userid,
            }
        )
        response_data = response.json()
        logging.debug(f"API response: {response_data}")
        return response_data
    except Exception as e:
        logging.error(f"Error making API request: {e}")


