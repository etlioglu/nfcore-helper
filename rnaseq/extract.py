"""
Extracts files of interest once an nfcore/rnaseq pipeline is finished.

"""

import typer

app = typer.Typer()

@app.command()
def extract():
    """
    Extract files of interest
    - count data (scaled by gene length)
    - variance stabilization transformed data
    """
    print("Creating the folder structure for an nfcore/rnaseq run")
