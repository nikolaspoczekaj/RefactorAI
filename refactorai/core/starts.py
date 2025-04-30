import json
from refactorai.ai import AIClient
import refactorai.helpers as helpers
from refactorai.logger import logger
from refactorai.core.refactor import refactor_file
import threading


def start_single_file(file_path: str) -> dict:
    
    logger.info(f"Refactoring {file_path}...")

    t = threading.Thread(target=refactor_file, args=(file_path,))
    t.start()
    t.join()

    logger.info(f"Refactored {file_path} successfully.")

