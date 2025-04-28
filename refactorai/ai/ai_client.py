from openai import OpenAI
import os
import json

class AIClient:
    def __init__(self, model):
        self.client = OpenAI(api_key=os.getenv("REFACTORAI_API_KEY"), base_url="https://api.deepseek.com")
        self.model = model
    
    def refactor_file(self, input_file, special_instructions=None):
        with open(input_file, 'r') as file:
            input = {"file": file,
                     "content": file.read(),
                     "special_instructions": special_instructions}
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Refactor the following code:\n{code}"}
            ],
            response_format={'type': 'json_object'}
        )
        
        refactored_code = response.choices[0].message['content']
        
        with open(output_file, 'w') as file:
            file.write(refactored_code)
