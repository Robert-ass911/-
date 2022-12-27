from sql_base import base_worker
from sql_base import models


def new_service(service: models.Services) -> int:
    new_id = base_worker.execute("INSERT INTO services(id, name, Price) "
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (service.id, service.name, service.Price))
    return