from refactorai.ai import AIClient
import json
import refactorai.helpers as helpers


def refactor_python_file(file_path: str) -> dict:
    ai_client = AIClient()

    with open(file_path, 'r') as file:
        input_file_content = file.read()

    output = ai_client.refactor_python_file(file_path, input_file_content)
    output = json.loads(output)

    with open(file_path, 'w') as file:
        file.write(output['content'])

    if not helpers.check_last_line(file_path):
        with open(file_path, 'a') as file:
            file.write("\n\n\n## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)")

    return output['changes_made']


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)