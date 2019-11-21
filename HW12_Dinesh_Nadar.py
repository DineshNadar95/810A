from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/Instructor_Summary')
def students_summary():

    DB_FILE = "E:\Assgnments\SSW 10\HomeWork11\810_HW11.db"
    query = """select instructors.CWID,instructors.Name,instructors.Dept,grades.Course,count(*) as students from instructors  join grades on instructors.CWID = grades.InstructorCWID
group by Course,CWID order by CWID;"""
    db = sqlite3.connect(DB_FILE)
    result = db.execute(query)
    data = [{'cwid': cwid, 'name': name, 'department': department, 'courses': courses, 'Students': Students}
            for cwid, name, department, courses, Students in result]
    db.close()

    return render_template('students_table.html', title="STEVENS Repository", table_title='Number of students by course and instructor', students=data)


app.run(debug=True)
