import os
import sys
import click

def check_api_key():
    api_key = os.getenv("REFACTORAI_API_KEY")
    if not api_key:
        click.echo("Error: env-variable REFACTORAI_API_KEY not set!", err=True)
        sys.exit(1)
    return api_key