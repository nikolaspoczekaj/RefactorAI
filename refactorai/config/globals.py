import os

class AppState:
    def __init__(self):
        self.PATH: str | None = None
        self.INTERACTIVE: bool | None = None
        self.RECURSIVE: bool = False
        
        self.MODEL: str | None = None
        self.SPECIAL_INSTRUCTIONS: str | None = None

        self.API_KEY: str | None = None
        self.API_URL: str | None = None

    def init_path(self, path: str | None) -> None:
        if path is None:
            self.PATH = os.getcwd()
        elif os.path.isdir(path):
            self.PATH = path
        elif os.path.isfile(path):
            self.PATH = path
        else:
            raise ValueError(f"'{path}' does not exist or is neither a file nor a directory.")

    def init_interactive(self, interactive: bool | None) -> None:
        if interactive is None:
            self.INTERACTIVE = False
        else:
            self.INTERACTIVE = interactive

    def init_recursive(self, recursive: bool | None) -> None:  
        if recursive is None:
            self.RECURSIVE = False
        else:
            self.RECURSIVE = recursive

    def init_model(self, model: str | None) -> None:
        if model is None:
            self.MODEL = "deepseek-chat"
        else:
            self.MODEL = model

    def init_special_instructions(self, special_instructions: str | None) -> None:
        self.SPECIAL_INSTRUCTIONS = special_instructions

    def init_api_url(self) -> None:
        self.API_URL = os.getenv("REFACTORAI_API_URL")
        if not self.API_URL:
            self.API_URL = input("Please enter API URL: ")

    def init_api_key(self) -> None:
        self.API_KEY = os.getenv("REFACTORAI_API_KEY")
        if not self.API_KEY:
            self.API_KEY = input("Please enter API key: ")
        
    def init(self, path: str | None, interactive: bool | None, recursive: bool | None, model: str | None, special_instructions: str | None) -> None:
        self.init_path(path)
        self.init_interactive(interactive)
        self.init_recursive(recursive)
        self.init_model(model)
        self.init_special_instructions(special_instructions)
        self.init_api_url()
        self.init_api_key()
    

    

    

STATE = AppState()