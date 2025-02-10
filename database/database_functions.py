import pyodbc

def insert_my_time_to_db(project_id, hours_worked, date, work_type):
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=PythonDatabase;'
        'UID=newuser;'  # Replace with your SQL Server username
        'PWD=test1234'  # Replace with your SQL Server password
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO MyTimeTracking (ProjectID, HoursWorked, Date, WorkType)
        VALUES (?, ?, ?, ?)
    """, project_id, hours_worked, date, work_type)
    conn.commit()
    cursor.close()
    conn.close()
    
