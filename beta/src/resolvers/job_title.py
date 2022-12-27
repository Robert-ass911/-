from sql_base import base_worker
from sql_base import models


def new_job_title(job_title: models.Job_title) -> int:
    new_id = base_worker.execute("INSERT INTO job_title(id, name) "
                                     "VALUES(?,?) "
                                     "RETURNING id",
                                     (job_title.id, job_title.name))
    return