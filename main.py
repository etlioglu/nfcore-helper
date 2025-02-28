import typer

from .rnaseq import app as rnaseq_app

app = typer.Typer()

app.add_typer(rnaseq_app, name="rnaseq")


if __name__ == "__main__":
    app()
