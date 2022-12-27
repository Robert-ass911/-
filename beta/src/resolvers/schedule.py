from sql_base import base_worker
from sql_base import models


def new_schedule(schedule: models.Schedule) -> int:
    new_id = base_worker.execute("INSERT INTO schedule(id, Work schedule, time_of_the_event, Pavilion) "
                                     "VALUES(?,?,?,?) "
                                     "RETURNING id",
                                     (schedule.id, schedule.Workschedule, schedule.time_of_the_event, schedule.Pavilion))
    return