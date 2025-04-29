from enum import Enum

class AIPrompts(Enum):
    """Enum class for AI prompts."""

    # Prompt for generating a Python function to calculate the sum of two numbers
    DEFAULT_REFACTOR = ("""
        Refactor the given Python code to comply with PEP 8, Python best practices, and any additional instructions provided. The input and output must be in JSON format, with the following structure:

Input JSON Structure:

{
    "name": "filename.py",  // or full path if applicable
    "content": "Original Python code here",
    "special_instructions": "Optional: Specific refactoring requests (e.g., 'use dataclasses', 'optimize loops', etc.)"
}
  
Output JSON Structure:

{
    "name": "filename.py",  // same as input
    "content": "Refactored Python code here",
    "changes_made": [
    "Fixed indentation (4 spaces per PEP 8)",
    "Renamed variables to snake_case",
    "Added type hints",
    "Optimized imports",
        "..."
    ]
}


Refactoring Guidelines (Follow Strictly):
PEP 8 Compliance:

4 spaces per indentation level

snake_case for variables/functions, PascalCase for classes

Maximum line length: 79 chars (or 88 if readability improves)

Proper spacing around operators and after commas

Best Practices:

Use isinstance() instead of type comparisons

Prefer list comprehensions over loops where readable

Remove unused imports/variables

Add type hints (if not present)

Break long functions/methods into smaller ones

Special Instructions:

If special_instructions are provided, prioritize them (e.g., "convert to async", "use dataclasses").

Output Clarity:

List all changes made in changes_made.


Example Input/Output:
Input:

{
    "name": "example.py",
    "content": "def calc(a,b):\n  return a+b\nclass MyClass:\n  def __init__(self,x):\n    self.x = x",
    "special_instructions": "Add type hints and docstrings"
}

Output:
                        
{
    "name": "example.py",
    "content": "def calc(a: int, b: int) -> int:\n    \"\"\"Add two integers and return the result.\"\"\"\n    return a + b\n\n\nclass MyClass:\n    \"\"\"Example class with typed attributes.\"\"\"\n\n    def __init__(self, x: int) -> None:\n        self.x = x",
    "changes_made": [
        "Added type hints to functions",
        "Added docstrings",
        "Fixed indentation (4 spaces)",
        "Added spacing around operators"
    ]
}

"""
    )

    
