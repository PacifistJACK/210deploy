from sqlalchemy import create_engine, text

# Database connection setup
engine = create_engine(
    "mysql+pymysql://freedb_jadu1:yu%21%40hrsBgSx9JZa@sql.freedb.tech:3306/freedb_jadukeproject1?charset=utf8mb4"
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
