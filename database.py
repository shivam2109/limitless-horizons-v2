import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    query = "SELECT * FROM jobs"
    result = conn.execute(text(query))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    query = f"SELECT * FROM jobs WHERE id = {id}"
    result = conn.execute(text(query))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()

def add_application_to_db(job_id,data):
  with engine.connect() as conn:
    query = f"INSERT INTO applications (job_id,full_name,email,linkedin_profile,education,work_experience,resume_url) VALUES ('{job_id}','{data['full_name']}','{data['email']}','{data['linkedin_profile']}','{data['education']}','{data['work_experience']}','{data['resume_url']}')"
    conn.execute(text(query))