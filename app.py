from flask import Flask, render_template, jsonify
from database import load_jobs, load_job_by_id

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
        return render_template('jobpg.html',job=job)
    else:
        return render_template('not.html'),404

if __name__ == "__main__":
    app.run(debug=True)
