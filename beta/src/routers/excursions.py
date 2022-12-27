from fastapi import APIRouter
from sql_base.models import Excursions
import resolvers.excursions

excursion_router = APIRouter()


@excursion_router.get('/')
def get_excursions():
    return f'Response: {{text: Страница со списком экскурсии }}'


@excursion_router.post('/')
def new_excursion(excursion: Excursions):
    new_id = resolvers.excursions.new_excursion(excursion)
    return f'{{code: 201, id: {new_id}}}'


@excursion_router.get('/{excursion_id}')
def get_excursion(excursion_id: int):
    excursion = resolvers.excursions.get_excursion(excursion_id)
    return f'excursion: {excursion}'


@excursion_router.put('/{excursion_id}')
def update_excursion(excursion: Excursions):
    excursion_id = resolvers.excursions.update_excursion(excursion)
    return f'Update excursion {excursion_id}'


@excursion_router.delete('/{excursion_id}')
def delete_excursion(excursion_id: int):
    excursion = resolvers.excursions.delete_excursion(excursion_id)
    return f'delete excursion {excursion_id}'