from flask import Flask, render_template, request, jsonify
from GeminiAiApiMethods import get_response, gemini_query_response
from datetime import datetime
from models.MyTimeModel import MyTimeModel
app = Flask(__name__, template_folder='views')

@app.route('/')
def home():
    return render_template('/Home/index.html')

@app.route('/my_time', methods=['GET', 'POST'])
def my_time():
    if request.method == 'POST':
        project_id = request.form['project_id']
        hours_worked = request.form['hours_worked']
        mytime_model = MyTimeModel(project_id=project_id, hours_worked=hours_worked)
        return render_template('/Home/my_time.html', mytime_model=mytime_model)
    else:
        return render_template('/Home/my_time.html', mytime_model=None)

@app.route('/gemini_query', methods=['POST'])

def gemini_query():
    query_response = gemini_query_response(request.get_json())
    return query_response

if __name__ == '__main__':
    app.run(debug=True)