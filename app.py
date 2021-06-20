from werkzeug.utils import redirect
from latex_actions import LatexDocument
import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/done', methods = ['GET', 'POST'])
def done():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    return '<h1>Done</h1>'

@app.route('/build', methods = ['GET', 'POST'])
def build():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    website = request.form.get('website')
    email = request.form.get('email')
    phone = request.form.get('phone')
    github = request.form.get('github')
    linkedin = request.form.get('linkedin')
    company_name = request.form.get('company_name')
    role = request.form.get('role')
    exp_city = request.form.get('exp_city')
    exp_country = request.form.get('exp_country')
    exp_start_month = request.form.get('exp_start_month')
    exp_start_year = request.form.get('exp_start_year')
    exp_end_month = request.form.get('exp_end_month')
    exp_end_year = request.form.get('exp_end_year')
    description = request.form.get('description')
    degree = request.form.get('degree')
    specialization = request.form.get('specialization')
    university = request.form.get('university')
    gpa = request.form.get('gpa')
    grad_city = request.form.get('grad_city')
    grad_country = request.form.get('grad_country')
    grad_month = request.form.get('grad_month')
    grad_year = request.form.get('grad_year')
    project_name = request.form.get('project_name')
    project_link = request.form.get('project_link')
    stack_description = request.form.get('stack_description')
    project_summary = request.form.get('project_summary')

    languages = request.form.get('languages')
    languages = languages.split(",")
    print(languages)
    technologies = request.form.get('technologies')
    technologies = technologies.split(",")
    print(technologies)
    courses = request.form.get('courses')
    courses = courses.split(",")
    print(courses)
    interests = request.form.get('interests')
    interests = interests.split(",")
    print(interests)

    doc = LatexDocument()
    doc.set_details(fname, lname, website, email, phone, github, linkedin)
    doc.make_experience_section(company_name, role, exp_city, exp_country, exp_start_month, exp_start_year, exp_end_month, exp_end_year, description)
    doc.make_education_section(degree, specialization, university, gpa, grad_city, grad_country, grad_month, grad_year)
    doc.make_projects_section(project_name, project_link, stack_description, project_summary)
    doc.make_skills_section(languages, technologies)
    doc.make_coursework_section(courses)
    doc.make_interests_section(interests)

    return redirect('/done')