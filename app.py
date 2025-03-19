from flask import Flask, render_template, redirect, url_for, request
from database import load_jobs, load_job_by_id, add_application

app = Flask(__name__)

# Homepage route
@app.route("/")
def home():
    jobs = load_jobs()
    return render_template('home.html', jobs=jobs)

# Job details route
@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_by_id(id)
    if job:
        return render_template('jobpg.html', job=job)
    else:
        return render_template('not.html'), 404

# Application form route
@app.route("/job/<int:id>/application")
def apply(id):
    job = load_job_by_id(id)
    if job:
        return render_template('application.html', job=job)
    else:
        return render_template('not.html'), 404

# Submit application route (fixed)
@app.route("/job/<int:id>/submit_application", methods=["POST"])
def submit_application(id):
    data = request.form
    job = load_job_by_id(id)
    if job:
        add_application(id, data)
        return render_template('application_submitted.html', application=data)
    else:
        return render_template('not.html'), 404



if __name__ == "__main__":
    app.run(debug=True)
