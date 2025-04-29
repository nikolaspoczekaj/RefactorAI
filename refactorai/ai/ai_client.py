from openai import OpenAI
import os
from refactorai.ai.prompts import AIPrompts


class AIClient:
    """Client for interacting with AI services for code refactoring."""

    def __init__(self, model: str) -> None:
        """Initialize the AI client with the specified model.
        
        Args:
            model: The AI model to use for refactoring.
        """
        self.client = OpenAI(
            api_key=os.getenv("REFACTORAI_API_KEY"),
            base_url="https://api.deepseek.com"
        )
        self.model = model
    
    def refactor_file(
        self,
        input_file_path: str,
        input_file_content: str,
        special_instructions: str = None
    ) -> str:
        """Refactor the given file content using the AI model.
        
        Args:
            input_file_path: Path to the input file.
            input_file_content: Content of the input file.
            special_instructions: Optional instructions for refactoring.
        
        Returns:
            The refactored content as a string.
        """
        input_data = {
            "file": input_file_path,
            "content": input_file_content,
            "special_instructions": special_instructions
        }
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": AIPrompts.DEFAULT_REFACTOR.value
                },
                {
                    "role": "user",
                    "content": f"{input_data}"
                }
            ],
            stream=False,
            max_tokens=8000,
            temperature=1.0,
            response_format={"type": "json_object"}
        )
        
        output = response.choices[0].message.content
        
        return output


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)