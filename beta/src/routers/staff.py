from fastapi import APIRouter
from sql_base.models import Staff
import resolvers.staff

staff_router = APIRouter()


@staff_router.get('/')
def get_staff():
    return f'Response: {{text: Страница со списком персонал }}'


@staff_router.post('/')
def new_staff(staff: Staff):
    new_id = resolvers.staff.new_staff(staff)
    return f'{{code: 201, id: {new_id}}}'


@staff_router.get('/{staff_id}')
def get_staff(staff_id: int):
    staff = resolvers.staff.get_staff(staff_id)
    return f'staff: {{id: {staff}}}'


@staff_router.put('/')
def update_staff(staff: Staff):
    staff_id = resolvers.staff.update_staff(staff)
    return f'Update staff {staff_id}'


@staff_router.delete('/{staff_id}')
def delete_staff(staff_id: int):
    staff = resolvers.staff.delete_staff(staff_id)
    return f'delete staff {staff_id}'