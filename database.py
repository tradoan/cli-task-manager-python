import sqlite3
from typing import List
import datetime
from model import ToDo

conn = sqlite3.connect("todo.db")
cursor = conn.cursor()


def create_table():
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS todo(
                task text,
                category text,
                date_added text,
                date_completed text,
                status int,
                position integer
            )
    """
    )


create_table()


def insert_todo(todo: ToDo):
    cursor.execute("SELECT COUNT(*) FROM todo")
    count = cursor.fetchone()[0]
    todo.position = count if count else 0
    print("count", count)

    with conn:
        cursor.execute(
            "INSERT INTO todo VALUES (:task, :category, :date_added, :date_completed, :status, :position)",
            {
                "task": todo.task,
                "category": todo.category,
                "date_added": todo.date_added,
                "date_completed": todo.date_completed,
                "status": todo.status,
                "position": todo.position,
            },
        )


def get_all_todos() -> List[ToDo]:
    cursor.execute("SELECT * from todo")
    results = cursor.fetchall()
    todos = []
    for result in results:
        todos.append(ToDo(*result))
    return todos


def delete_todo(position):
    cursor.execute("SELECT COUNT(*) from todo")
    count = cursor.fetchone()[0]
    print("count", count)

    with conn:
        cursor.execute(
            "DELETE FROM todo WHERE position=:position", {"position": position}
        )

        for pos in range(position + 1, count):
            change_position(pos, pos - 1, False)


def change_position(old_pos, new_pos, commit=True):
    cursor.execute(
        "UPDATE todo SET position=:new_pos WHERE position=:old_pos",
        {"old_pos": old_pos, "new_pos": new_pos},
    )

    if commit:
        conn.commit()


def update_todo(position: int, task: str, category: str):
    with conn:
        if task and category:
            cursor.execute(
                "UPDATE todo SET task=:task, category=:category WHERE position=:position",
                {"task": task, "category": category, "position": position},
            )
        if task:
            cursor.execute(
                "UPDATE todo SET task=:task WHERE position=:position",
                {"task": task, "position": position},
            )
        if category:
            cursor.execute(
                "UPDATE todo SET category=:category WHERE position=:position",
                {"task": task, "position": position},
            )


def complete_todo(position: int):
    with conn:
        cursor.execute(
            "UPDATE todo SET status = 2, date_completed = :date_completed WHERE position = :position",
            {
                "position": position,
                "date_completed": datetime.datetime.now().isoformat(),
            },
        )


def clear_all():
    with conn:
        cursor.execute("DELETE FROM todo;")
