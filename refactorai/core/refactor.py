from refactorai.ai import AIClient
import json
import refactorai.helpers as helpers

def refactor_file(file_path: str, model: str, special_instructions: str = None) -> dict:
    """
    Refactor a single file using the specified AI model and special instructions.

    Args:
        file_path (str): The path to the file to be refactored.
        model (str): The AI model to use for refactoring.
        special_instructions (str, optional): Special instructions for the AI model.

    Returns:
        dict: A dictionary containing the changes made to the file.
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