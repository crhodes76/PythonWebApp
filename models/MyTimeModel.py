import random
import string

class MyTimeModel:
    def __init__(self, project_id=None, hours_worked=None):
        self.project_id = project_id
        self.hours_worked = hours_worked
        self.project_ids = [''.join(random.choices(string.ascii_letters + string.digits, k=8)) for _ in range(5)]