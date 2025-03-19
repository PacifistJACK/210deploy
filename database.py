from sqlalchemy import create_engine, text

# Database connection setup
db_connection_link = "mysql://avnadmin:AVNS_e2hoDjCqTFYQ0_LCs6u@mysql-3c88c130-careerappp.l.aivencloud.com:25216/defaultdb"

# Correct SSL configuration in connect_args
engine = create_engine(
    db_connection_link,
    connect_args={
        "ssl": {
            "ca": r"D:\maderchodh\kare\210deploy\ca.pem"  # Raw string to avoid escape issues
        }
    }
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
        return dict(row._mapping) if row else None

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
