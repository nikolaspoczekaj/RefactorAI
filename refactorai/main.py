import os

import click

import refactorai.core as core
import refactorai.helpers as helpers


@click.group()
def main() -> None:
    """RefactorAI CLI – AI-driven refactoring tool."""
    pass


@main.command()
@click.option("--path", "-p", default=".", help="path of the file/directory (default: current directory)")
@click.option("--recursive", "-r", is_flag=True, help="path to the file to be refactored")
@click.option("--model", "-m", default="deepseek-chat", show_default=True, help="AI-model")
@click.option("--interactive", "-i", is_flag=True, help="manually accept changes")
def run(path: str, recursive: bool, model: str, interactive: bool) -> None:
    """Starte das Refactoring im angegebenen Projektpfad."""
    helpers.check_api_key()

    click.echo(f"Starte Refactoring für {path}")

    if os.path.isdir(path):
        click.echo(f"'{path}' ist ein Verzeichnis (Ordner).")
        click.echo("Processing of whole directory isn't implemented yet. Please specify a file...")
    elif os.path.isfile(path):
        click.echo(f"'{path}' ist eine Datei.")
        print(core.start_single_file(path, model))
    else:
        click.echo(f"'{path}' existiert nicht oder ist weder eine Datei noch ein Ordner.")


@main.command()
@click.option("--path", "-p", default=".", help="Pfad zum Python-Projekt (Standard: aktuelles Verzeichnis)")
def check(path: str) -> None:
    """Überprüfe mögliche Refactorings, ohne Änderungen vorzunehmen."""
    api_key = helpers.check_api_key()
    click.echo(f"Check-Modus für {path}")
    # Hier Logic für Check (Analyse, aber kein Refactor)


if __name__ == "__main__":
    main()
