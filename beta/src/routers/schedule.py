from fastapi import APIRouter
from sql_base.models import Schedule
import resolvers.schedule

schedule_router = APIRouter()


@schedule_router.get('/')
def get_schedule():
    return f'Response: {{text: Страница со списком график }}'


@schedule_router.post('/')
def new_schedule(schedule: Schedule):
    new_id = resolvers.schedule.new_schedule(schedule)
    return f'{{code: 201, id: {new_id}}}'


@schedule_router.get('/{schedule_id}')
def get_schedule(schedule_id: int):
    schedule = resolvers.schedule.get_schedule(schedule_id)
    return f'schedule: {{id: {schedule}}}'


@schedule_router.put('/')
def update_schedule(schedule: Schedule):
    schedule_id = resolvers.schedule.update_schedule(schedule)
    return f'Update schedule {schedule_id}'


@schedule_router.delete('/{schedule_id}')
def delete_schedule(schedule_id: int):
    schedule = resolvers.schedule.delete_schedule(schedule_id)
    return f'delete schedule {schedule_id}'