import os
import click
import refactorai.core as core
from refactorai.logger import logger
from refactorai.config import STATE


@click.command()
@click.argument("path", default=".")
@click.option("--recursive", "-r", is_flag=True, help="Recursively process directories")
@click.option("--model", "-m", default="deepseek-chat", show_default=True, help="AI model to use")
@click.option("--interactive", "-i", is_flag=True, help="Manually accept changes")
@click.option("--special-instructions", "-s", default=None, help="Special instructions for the AI model")
def main(path: str, recursive: bool, model: str, interactive: bool, special_instructions: str | None) -> None:
    """RefactorAI CLI - AI-driven refactoring tool."""
    STATE.init(path, interactive, recursive, model, special_instructions)

    if os.path.isdir(STATE.path) and STATE.recursive:
        logger.info(f"Processing directory recursively: {STATE.path}")
        core.start_directory_recursive(STATE.path)
    elif os.path.isdir(STATE.path):
        logger.warning(f"'{STATE.path}' is a directory but recursive mode is not enabled. Use -r to process recursively.")
    elif os.path.isfile(STATE.path):
        logger.info(f"Processing single file: {STATE.path}")
        core.start_single_file(STATE.path)
    else:
        logger.error(f"'{STATE.path}' does not exist or is not accessible.")


if __name__ == "__main__":
    main()


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)