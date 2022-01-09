import typer
from rich.console import Console
from rich.table import Table
from model import ToDo
from database import (
    update_todo,
    insert_todo,
    delete_todo,
    complete_todo,
    get_all_todos,
    clear_all,
)

console = Console()
app = typer.Typer()


@app.command(short_help="adds an item")
def add(task: str, category: str):
    typer.echo(f"adding")
    new_todo = ToDo(task, category)
    insert_todo(new_todo)
    show()


@app.command(short_help="delete an item")
def delete(position: int):
    typer.echo(f"deleting {position}")
    delete_todo(position - 1)
    show()


@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    complete_todo(position - 1)
    show()


@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    update_todo(position - 1, task, category)
    show()


@app.command()
def show():
    todos = get_all_todos()
    console.print("[bold magenta]Todos[/bold magenta]!", "👩‍💻")

    table = Table(show_header=True, header_style="bold")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Status", min_width=8, justify="right")
    table.add_column("Created At", min_width=8, justify="right")
    table.add_column("Completed At", min_width=8, justify="right")

    def get_category_color(category):
        COLORS = {
            "Learn": "yellow",
            "Youtube": "red",
            "Sport": "cyan",
            "Study": "green",
            "Shoping": "yellow",
        }
        if category in COLORS:
            return COLORS[category]
        return "white"

    for todo in todos:
        color = get_category_color(todo.category)
        status_icon = "✅" if todo.status else "❌"

        table.add_row(
            str(todo.position + 1),
            todo.task,
            f"[{color}]{todo.category}[{color}]",
            status_icon,
            todo.date_added,
            todo.date_completed,
        )
    console.print(table)


@app.command()
def clean():
    typer.echo(f"clean list")
    clear_all()
    show()


if __name__ == "__main__":
    app()
