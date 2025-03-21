import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()

# Get database connection link from environment variables
db_connection_link = os.getenv("DB_CONNECTION_LINK")
db_connection_link = db_connection_link.strip('"')

# Path to CA certificate stored as a secret file in Render
ca_cert_path = "/etc/secrets/ca.pem"  

# Check if CA certificate file exists
if not os.path.exists(ca_cert_path):
    raise ValueError(f"CA certificate file not found at {ca_cert_path}")

# Create database engine with SSL using the CA certificate file
engine = create_engine(
    db_connection_link,
    connect_args={"ssl": {"ca": ca_cert_path}}  # Pass the file path
)

# Function to load all jobs into a list of dictionaries
def load_jobs():
    jobs_list = []
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        for row in result:
            jobs_list.append(dict(row._mapping))
    return jobs_list

# Function to load a specific job by ID
def load_job_by_id(job_id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val": job_id}
        )
        row = result.fetchone()
        if row:
            job = dict(row._mapping)
            
            # Properly format responsibilities & requirements
            job['responsibities'] = "\n".join(filter(None, re.split(r"\.\s+|\n+", job['responsibities'])))
            job['requirements'] = "\n".join(filter(None, re.split(r"\.\s+|\n+", job['requirements'])))

            return job
        return None


# Function to add a job application
def add_application(job_id, application):
    with engine.connect() as conn:
        query = text("""
            INSERT INTO applications (job_id, name, email, linkedin, education, experience, resume)
            VALUES (:job_id, :name, :email, :linkedin, :education, :experience, :resume)
        """)
        conn.execute(query, {
            'job_id': job_id,
            'name': application['name'],
            'email': application['email'],
            'linkedin': application['linkedin'],
            'education': application['education'],
            'experience': application['experience'],
            'resume': application['resume']
        })
        conn.commit()
