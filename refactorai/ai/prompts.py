from enum import Enum


class AIPrompts(Enum):
    """Enum class for AI prompts."""

    DEFAULT_PYTHON_REFACTOR = (
        """
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

                        
ADDITIONAL INSTUCTIONS:
    
    NEVER OUTPUT ANYTHING BUT JSON. DO NOT ADD ANY TEXT, COMMENTS, OR EXPLANATIONS OUTSIDE OF THE JSON STRUCTURE !!!
    IF THE INPUT CODE IS ALREADY PERFECT, RETURN THE SAME JSON STRUCTURE WITHOUT ANY MODIFICATIONS AND AN EMPTY CHANGES_MADE LIST.
    ONLY UTF-8 CHARACTERS ARE ALLOWED.
    DONT EVER CHANGE FUNCTIONALLITY OR LOGIC OF THE CODE.
    REMOVE ALL UNUSED IMPORTS AND VARIABLES. 
"""
    )


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)