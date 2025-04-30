import threading

from refactorai.ai import AIClient
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


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)