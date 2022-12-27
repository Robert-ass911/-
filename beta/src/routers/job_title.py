from fastapi import APIRouter
from sql_base.models import Job_title
import resolvers.job_title

job_title_router = APIRouter()


@job_title_router.get('/')
def get_job_title():
    return f'Response: {{text: Страница со списком должность }}'


@job_title_router.post('/')
def new_job_title(job_title: Job_title):
    new_id = resolvers.job_title.new_job_title(job_title)
    return f'{{code: 201, id: {new_id}}}'


@job_title_router.get('/{job_title_id}')
def get_job_title(job_title_id: int):
    job_title = resolvers.job_title.get_job_title(job_title_id)
    return f'job_title: {{id: {job_title}}}'


@job_title_router.put('/')
def update_job_title(job_title: Job_title):
    job_title_id = resolvers.job_title.update_job_title(job_title)
    return f'Update job_title {job_title_id}'


@job_title_router.delete('/{job_title_id}')
def delete_job_title(job_title_id: int):
    job_title = resolvers.job_title.delete_job_title(job_title_id)
    return f'delete job_title {job_title_id}'