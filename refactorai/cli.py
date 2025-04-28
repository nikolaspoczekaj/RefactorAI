import click
import os
import sys

def check_api_key():
    api_key = os.getenv("REFACTORAI_API_KEY")
    if not api_key:
        click.echo("Error: env-variable REFACTORAI_API_KEY not set!", err=True)
        sys.exit(1)
    return api_key

@click.group()
def cli():
    """RefactorAI CLI – AI-driven refactoring tool."""
    pass

@cli.command()
@click.option("--path", "-p", default=".", help="directory of the project (default: current directory)")
@click.option("--model", "-m", default="deepseek-chat", show_default=True, help="AI-model")
@click.option("--strategy", "-s", default="basic", show_default=True, type=click.Choice(['basic', 'advanced', 'custom']), help="Refactoring strategy")
@click.option("--interactive", "-i", is_flag=True, help="manually accept changes")
def run(path, model, strategy, interactive):
    """Starte das Refactoring im angegebenen Projektpfad."""
    api_key = check_api_key()

    click.echo(f"Starte Refactoring für {path}")
    click.echo(f"model: {model} | strategy: {strategy} | interactive: {interactive}")
    
    # Hier kommt deine Refactoring-Logik hin!
    # z.B.: refactorai.core.refactor_project(path, ...)

@cli.command()
@click.option("--path", "-p", default=".", help="Pfad zum Python-Projekt (Standard: aktuelles Verzeichnis)")
def check(path):
    """Überprüfe mögliche Refactorings, ohne Änderungen vorzunehmen."""
    api_key = check_api_key()
    click.echo(f"Check-Modus für {path}")
    # Hier Logic für Check (Analyse, aber kein Refactor)

if __name__ == "__main__":
    cli()
