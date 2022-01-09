import datetime


class ToDo:
    def __init__(
        self,
        task,
        category,
        date_added=None,
        date_completed=None,
        status=0,
        position=None,
    ):
        self.task = task
        self.category = category
        self.date_added = (
            date_added if date_added else datetime.datetime.now().isoformat()
        )
        self.date_completed = date_completed
        self.status = status
        self.position = position

    def __repr__(self):
        return f"{self.task}, {self.category}, {self.date_added}, {self.date_completed}, {self.status}, {self.position}"
