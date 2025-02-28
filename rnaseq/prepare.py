"""
Creates a folder structure for nfcore/rnaseq runs as well as associated files
(Nextflow command, nf_params.json) required to run the pipeline.
"""

from pathlib import Path

import typer


def _create_folder(folder_path: Path) -> None:
    try:
        folder_path.mkdir()
        print(f"Directory '{folder_path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{folder_path}' already exists.")
        raise typer.Exit()
    except PermissionError:
        print(f"Permission denied: Unable to create '{folder_path}'.")
        raise typer.Exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        raise typer.Exit()


app = typer.Typer()


@app.command()
def prepare_folders():
    """
    Create folders
    - A parent folder, nfcore_rnaseq
    - A child folder, prepare_samplesheet, that holds a sample sheet for the
    run as well as a code template to generate one
    - A child folder, nfcore_rnaseq_output, that serves as the "output" folder
    for an nfcore_rnaseq run
    """

    print("Creating the folder structure for an nfcore/rnaseq run")

    # parent folder: ./nfcore_rnaseq
    nfcore_rnaseq_path = Path("nfcore_rnaseq")
    _create_folder(nfcore_rnaseq_path)

    # child folder: ./nfcore_rnaseq/prepare_samplesheet
    prepare_samplesheet_path = nfcore_rnaseq_path / "prepare_samplesheet"
    _create_folder(prepare_samplesheet_path)

    # child folder: ./nfcore_rnaseq/nfcore_rnaseq_output
    nfcore_rnaseq_output_path = nfcore_rnaseq_path / "rnaseq_output"
    _create_folder(nfcore_rnaseq_output_path)


def _create_nextflow():
    pass

def _create_params():
    pass

@app.command()
def prepare_files():
    """
    Create files to run the pipeline
    - nextflow_command.txt: Nextflow command to run the nfcore/rnaseq pipeline
    - nf_params.json: Settings file referenced by the nextflow_command.txt file
    above
    """
    print("Creating necessary files required to run an nfcore/rnaseq pipeline")
