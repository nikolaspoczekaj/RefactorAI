import os


class AppState:
    def __init__(self):
        self.path: str | None = None
        self.interactive: bool | None = None
        self.recursive: bool = False
        self.model: str | None = None
        self.special_instructions: str | None = None
        self.api_key: str | None = None
        self.api_url: str | None = None

    def init_path(self, path: str | None) -> None:
        if path is None:
            self.path = os.getcwd()
        elif os.path.isdir(path):
            self.path = path
        elif os.path.isfile(path):
            self.path = path
        else:
            raise ValueError(f"'{path}' does not exist or is neither a file nor a directory.")

    def init_interactive(self, interactive: bool | None) -> None:
        if interactive is None:
            self.interactive = False
        else:
            self.interactive = interactive

    def init_recursive(self, recursive: bool | None) -> None:
        if recursive is None:
            self.recursive = False
        else:
            self.recursive = recursive

    def init_model(self, model: str | None) -> None:
        if model is None:
            self.model = "deepseek-chat"
        else:
            self.model = model

    def init_special_instructions(self, special_instructions: str | None) -> None:
        self.special_instructions = special_instructions

    def init_api_url(self) -> None:
        self.api_url = os.getenv("REFACTORAI_API_URL")
        if not self.api_url:
            self.api_url = input("Please enter API URL: ")

    def init_api_key(self) -> None:
        self.api_key = os.getenv("REFACTORAI_API_KEY")
        if not self.api_key:
            self.api_key = input("Please enter API key: ")

    def init(
        self,
        path: str | None,
        interactive: bool | None,
        recursive: bool | None,
        model: str | None,
        special_instructions: str | None,
    ) -> None:
        self.init_path(path)
        self.init_interactive(interactive)
        self.init_recursive(recursive)
        self.init_model(model)
        self.init_special_instructions(special_instructions)
        self.init_api_url()
        self.init_api_key()


STATE = AppState()


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)