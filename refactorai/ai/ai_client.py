from openai import OpenAI
import os
import json
from refactorai.ai.prompts import AIPrompts

class AIClient:
    def __init__(self, model):
        self.client = OpenAI(api_key=os.getenv("REFACTORAI_API_KEY"), base_url="https://api.deepseek.com")
        self.model = model
    
    def refactor_file(self, input_file_path, input_file_content, special_instructions=None):
        
        input = {"file": input_file_path,
                "content": input_file_content,
                "special_instructions": special_instructions}
        
        print(input)
        
        response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": AIPrompts.DEFAULT_REFACTOR.value},
                    {"role": "user", "content": f"{input}"}
                ],
                stream=False,
                max_tokens=8000,
                temperature=1.0,
                response_format={'type': 'json_object'}
            )
        
        output = json.loads(response.choices[0].message.content)
        
        return output
