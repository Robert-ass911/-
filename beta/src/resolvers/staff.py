from sql_base import base_worker
from sql_base import models


def new_staff(staff: models.Staff) -> int:
    new_id = base_worker.execute("INSERT INTO staff(id, Full_name, Post, Salary, Education, Phone number) "
                                     "VALUES(?,?,?,?,?,?) "
                                     "RETURNING id",
                                     (staff.id, staff.Full_name, staff.Post, staff.Salary, staff.Education, staff.Phonenumber))
    return