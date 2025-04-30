import os
import sys
import click


def check_api_key() -> None:
    api_key = os.getenv("REFACTORAI_API_KEY")
    if not api_key:
        click.echo("Error: env-variable REFACTORAI_API_KEY not set!", err=True)
        sys.exit(1)


def check_last_line(file_path: str) -> bool:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            last_line = None
            for line in file:
                line = line.strip()
                if line:
                    last_line = line

            if last_line is None:
                return False

            return 'refactored by RefactorAI' in last_line
    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return False


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)