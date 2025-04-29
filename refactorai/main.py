import os

import click

import refactorai.core as core
import refactorai.helpers as helpers
from refactorai.logger import logger


@click.group()
def main() -> None:
    """RefactorAI CLI - AI-driven refactoring tool."""
    pass


@main.command()
@click.option("--path", "-p", default=".", help="path of the file/directory (default: current directory)")
@click.option("--recursive", "-r", is_flag=True, help="path to the file to be refactored")
@click.option("--model", "-m", default="deepseek-chat", show_default=True, help="AI-model")
@click.option("--interactive", "-i", is_flag=True, help="manually accept changes")
def run(path: str, recursive: bool, model: str, interactive: bool) -> None:
    """Start refactoring."""
    helpers.check_api_key()


    if os.path.isdir(path):
        logger.warning(f"'{path}' ist ein Verzeichnis (Ordner).")
        logger.warning("Processing of whole directory isn't implemented yet. Please specify a file...")
    elif os.path.isfile(path):
        logger.info(f"'{path}' ist eine Datei.")
        logger.info(core.start_single_file(path, model))
    else:
        logger.error(f"'{path}' existiert nicht oder ist weder eine Datei noch ein Ordner.")


@main.command()
@click.option("--path", "-p", default=".", help="Pfad zum Python-Projekt (Standard: aktuelles Verzeichnis)")
def check(path: str) -> None:
    api_key = helpers.check_api_key()
    # Hier Logic f�r Check (Analyse, aber kein Refactor)


if __name__ == "__main__":
    main()