from sqlalchemy import create_engine, text

# Database connection setup
engine = create_engine(
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
