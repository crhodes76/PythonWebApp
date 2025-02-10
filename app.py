from flask import Flask, render_template, request, jsonify
from GeminiAiApiMethods import get_response, gemini_query_response
from models.MyTimeModel import MyTimeModel
from database.database_functions import insert_my_time_to_db

app = Flask(__name__, template_folder='views')

@app.route('/')
def home():
    return render_template('/Home/index.html')


@app.route('/my_time', methods=['GET', 'POST'])
def my_time():
    mytime_model = MyTimeModel()
    if request.method == 'POST':
        project_id = request.form['project_id']
        hours_worked = request.form['hours_worked']
        date = request.form['date']
        work_type = request.form['work_type']
        mytime_model.project_id = project_id
        mytime_model.hours_worked = hours_worked
        mytime_model.date = date
        mytime_model.work_type = work_type
        insert_my_time_to_db(project_id, hours_worked, date, work_type)
    return render_template('/Home/my_time.html', mytime_model=mytime_model)

@app.route('/gemini_query', methods=['POST'])
def gemini_query():
    query_response = gemini_query_response(request.get_json())
    return query_response

if __name__ == '__main__':
    app.run(debug=True)