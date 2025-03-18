from flask import Flask, render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)

#adding dummy data

def load_job():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

        Jobs = [dict(row._mapping) for row in result]
        return Jobs

@app.route("/")
def hello_world():
    Jobs = load_job()
    return render_template('home.html', jobs = Jobs)

if __name__ == "__main__":
    app.run(debug=True)