from fastapi import APIRouter
from sql_base.models import Services
import resolvers.services

service_router = APIRouter()


@service_router.get('/')
def get_services():
    return f'Response: {{text: Страница со списком услуги }}'


@service_router.post('/')
def new_service(service: Services):
    new_id = resolvers.services.new_service(service)
    return f'{{code: 201, id: {new_id}}}'


@service_router.get('/{service_id}')
def get_service(service_id: int):
    service = resolvers.services.get_employee(service_id)
    return f'service: {service}'


@service_router.put('/{service_id}')
def update_service(service: Services):
    service_id = resolvers.services.update_service(service)
    return f'Update service {service_id}'


@service_router.delete('/{service_id}')
def delete_service(service_id: int):
    service = resolvers.services.delete_service(service_id)
    return f'delete service {service_id}'