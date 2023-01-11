from sql_base import base_worker
from sql_base import models


def new_exhibit(exhibit: models.Exhibits) -> int:
    new_id = base_worker.execute("INSERT INTO exhibits(id, name, Quantity, Date_of_receipt, Condition, author, material) "
                                     "VALUES(?,?,?,?,?,?,?) "
                                     "RETURNING id",
                                     (exhibit.id, exhibit.name, exhibit.Quantity, exhibit.Date_of_receipt, exhibit.Condition, exhibit.author, exhibit.material))
    return new_id
