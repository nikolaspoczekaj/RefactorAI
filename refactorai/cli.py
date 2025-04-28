import click
import os
import sys

# Wichtige Hilfsfunktion zum Checken des API Keys
def check_api_key():
    api_key = os.getenv("REFACTORAI_API_KEY")
    if not api_key:
        click.echo("Fehler: Umgebungsvariable REFACTORAI_API_KEY nicht gesetzt!", err=True)
        sys.exit(1)
    return api_key

@click.group()
def cli():
    """RefactorAI CLI – AI-driven refactoring tool."""
    pass

@cli.command()
@click.option("--path", "-p", default=".", help="directory of the project (default: current directory)")
@click.option("--model", "-m", default="gpt-4", show_default=True, help="KI-Modell (z.B. gpt-4, claude-3)")
@click.option("--strategy", "-s", default="basic", show_default=True, type=click.Choice(['basic', 'advanced', 'custom']), help="Refactoring-Strategie")
@click.option("--interactive", "-i", is_flag=True, help="Bestätige jede Änderung manuell")
@click.option("--dry-run", is_flag=True, help="Nur Vorschau der Änderungen (kein Schreiben)")
def run(path, model, strategy, interactive, dry_run):
    """Starte das Refactoring im angegebenen Projektpfad."""
    api_key = check_api_key()

    click.echo(f"Starte Refactoring für {path}")
    click.echo(f"Modell: {model} | Strategie: {strategy} | Dry-Run: {dry_run} | Interaktiv: {interactive}")
    
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
