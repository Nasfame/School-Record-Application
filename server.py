from flask import Flask, request
import csv,json,jwt,time
from blueprint_teacher import staff
from blueprint_student import student
from blueprint_school import school

app = Flask(__name__)
app.register_blueprint(staff,url_prefix='/staff')
app.register_blueprint(student,url_prefix='/student')
app.register_blueprint(school,url_prefix='/school')
@app.route('/')
def welcome() :
    return json.dumps('Welcome to Our school')

if __name__ == '__main__' :
    app.run(debug=True)
