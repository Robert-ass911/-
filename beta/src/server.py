from fastapi import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from routers.excursions import excursion_router
from routers.exhibits import exhibit_router
from routers.services import service_router
from routers.Schedule import Schedule_router
from routers.staff import staff_router
from routers.job_title import job_title_router


base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base('../sql/base.sql')

app = FastAPI()


@app.get("/")
def main_page():
    return {'page': 'Connection in correct'}


app.include_router(excursion_router, prefix='/excursions')
app.include_router(exhibit_router, prefix='/exhibits')
app.include_router(service_router, prefix='/services')
app.include_router(Schedule_router, prefix='/Schedule')
app.include_router(staff_router, prefix='/staff')
app.include_router(job_title_router, prefix='/job_title')
