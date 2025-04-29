import json
from refactorai.ai import AIClient
import refactorai.helpers as helpers


def start_single_file(file_path: str, model: str, special_instructions: str = None) -> dict:
    """Refactor a single file using the specified AI model.
    
    Args:
        file_path: Path to the file to refactor.
        model: The AI model to use for refactoring.
        special_instructions: Optional instructions for the AI.
    
    Returns:
        A dictionary of changes made by the AI.
    """
    ai_client = AIClient(model=model)

    with open(file_path, 'r') as file:
        input_file_content = file.read()

    output = ai_client.refactor_file(file_path, input_file_content, special_instructions)
    output = json.loads(output)

    with open(file_path, 'w') as file:
        file.write(output['content'])

    if not helpers.check_last_line(file_path):
        with open(file_path, 'a') as file:
            file.write("\n\n\n## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)")

    return output['changes_made']


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)