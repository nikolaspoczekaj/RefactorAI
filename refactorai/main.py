import os

import click

import refactorai.core as core
import refactorai.helpers as helpers
from refactorai.logger import logger
from refactorai.config import STATE


@click.group()
def main() -> None:
    """RefactorAI CLI - AI-driven refactoring tool."""
    pass


@main.command()
@click.option("--path", "-p", default=".", help="path of the file/directory (default: current directory)")
@click.option("--recursive", "-r", is_flag=True, help="path to the file to be refactored")
@click.option("--model", "-m", default="deepseek-chat", show_default=True, help="AI-model")
@click.option("--interactive", "-i", is_flag=True, help="manually accept changes")
@click.option("--special-instructions", "-s", default=None, help="special instructions for the AI model")
def run(path: str, recursive: bool, model: str, interactive: bool, special_instructions: str | None) -> None:
    """Start refactoring."""
    STATE.init(path, interactive, recursive, model, special_instructions)


    if os.path.isdir(STATE.PATH) and STATE.RECURSIVE:
        logger.warning(f"{STATE.PATH} is a directory.")
        core.start_directory_recursive(STATE.PATH)
    elif os.path.isfile(STATE.PATH):
        logger.info(f"{STATE.PATH} is a single file.")
        core.start_single_file(STATE.PATH)
    else:
        logger.error(f"'{STATE.PATH}' does not exist or is neither a file nor a directory.")




if __name__ == "__main__":
    main()