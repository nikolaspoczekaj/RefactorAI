import threading
import os
from typing import List
from pathlib import Path
from refactorai.logger import logger
from refactorai.core.refactor import refactor_python_file


def start_single_file(file_path: str) -> dict:
    """Refactor a single file using a separate thread.
    
    Args:
        file_path: Path to the file to be refactored.
    
    Returns:
        dict: The result of the refactoring process.
    """
    logger.info(f"Refactoring {file_path}...")

    thread = threading.Thread(target=refactor_python_file, args=(file_path,))
    thread.start()
    thread.join()

    logger.info(f"Refactored {file_path} successfully.")


def start_directory_recursive(directory_path: str) -> None:
    """Refactors all .py files in a directory recursively using separate threads.
    
    Args:
        directory_path: Path to the directory to be scanned for .py files.
    """
    py_files = [str(path) for path in Path(directory_path).rglob("*.py")]
    
    if not py_files:
        logger.info(f"No Python files found in {directory_path}.")
        return

    logger.info(f"Found {len(py_files)} Python files to refactor in {directory_path}...")

    threads: List[threading.Thread] = []
    for file_path in py_files:
        thread = threading.Thread(
            target=start_single_file,
            args=(file_path,),
            name=f"RefactorThread-{os.path.basename(file_path)}"
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    logger.info(f"Finished refactoring all {len(py_files)} Python files in {directory_path}.")


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)