from datetime import date, datetime

class MyTimeModel:
    def __init__(self, project_id=None, hours_worked=None, date=None, work_type=None):
        self.project_id = project_id
        self.hours_worked = hours_worked
        self.date = date or datetime.today().strftime('%Y-%m-%d')
        self.work_type = work_type
        self.project_ids = ['A1A8', 'A1A7', 'A1A6', 'A1A5', 'A1A4']