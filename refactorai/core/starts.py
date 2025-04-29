import json

def start_single_file(file_path: str, model: str, special_instructions: str = None) -> dict:
    
    from refactorai.ai import AIClient

    ai_client = AIClient(model=model)

    # Read file content
    with open(file_path, 'r') as file:
        input_file_content = file.read()

    # Call AI client to refactor the file
    output = ai_client.refactor_file(file_path, input_file_content, special_instructions)
    print(output)
    output = json.loads(output)
    
    with open(file_path, 'w') as file:
        file.write(output['content'])

    return output['changes_made']