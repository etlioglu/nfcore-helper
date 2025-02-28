import typer

from .prepare import app as prepare_app
from .extract import app as extract_app

app = typer.Typer()

app.add_typer(prepare_app)
app.add_typer(extract_app)
