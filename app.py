from flask import Flask, render_template

app = Flask(__name__)

#adding dummy data

Jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Raipur, India',
        'salary': '10,000,000'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'Bangalore, India',
        'salary': '20,000,000'
    },
    {
        'id': 3,
        'title': 'Python Developer',
        'location': 'Remote',
        'salary': '12,000,000'
    },
    {
        'id': 4,
        'title': 'AI Engineer',
        'location': 'Gurugram, India',
        'salary': '30,000,000'
    },
    {
        'id': 5,
        'title': 'Web Developer',
        'location': 'Remote',
        'salary': '5,000,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs = Jobs)

if __name__ == "__main__":
    app.run(debug=True)
