from sql_base import base_worker
from sql_base import models


def new_excursion(excursion: models.Excursions) -> int:
    new_id = base_worker.execute("INSERT INTO excursions(id, event, Chart, cost) "
                                     "VALUES(?,?,?,?) "
                                     "RETURNING id",
                                     (excursion.id, excursion.event, excursion.Chart, excursion.cost))
    return new_id
