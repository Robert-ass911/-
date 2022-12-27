from fastapi import APIRouter
from sql_base.models import Exhibits
import resolvers.exhibits

exhibit_router = APIRouter()


@exhibit_router.get('/')
def get_exhibits():
    return f'Response: {{text: Страница со списком экспонаты }}'


@exhibit_router.post('/')
def new_exhibit(exhibit: Exhibits):
    new_id = resolvers.exhibits.new_exhibit(exhibit)
    return f'{{code: 201, id: {new_id}}}'


@exhibit_router.get('/{exhibit_id}')
def get_exhibit(exhibit_id: int):
    exhibit = resolvers.exhibits.get_exhibit(exhibit_id)
    return f'exhibit: {exhibit}'


@exhibit_router.put('/{exhibit_id}')
def update_exhibit(exhibit: Exhibits):
    exhibit_id = resolvers.exhibits.update_exhibit(exhibit)
    return f'Update exhibit {exhibit_id}'


@exhibit_router.delete('/{exhibit_id}')
def delete_exhibit(exhibit_id: int):
    exhibit = resolvers.exhibits.delete_exhibit(exhibit_id)
    return f'delete exhibit {exhibit_id}'