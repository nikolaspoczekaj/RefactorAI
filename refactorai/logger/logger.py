from rich.console import Console
from rich.theme import Theme
from rich.logging import RichHandler
import logging

theme = Theme({
    "info": "dim cyan",
    "warning": "gold3",
    "error": "bold red",
    "success": "bold green",
    "debug": "gray50",
})

console = Console(theme=theme)

def setup_logging(level: int = logging.INFO) -> logging.Logger:
    logging.basicConfig(
        level=level,
        format="%(message)s",
        handlers=[RichHandler(console=console, show_time=False, show_level=True, markup=True)],
    )
    return logging.getLogger("refactorai")

logger = setup_logging()


## refactored by RefactorAI (https://github.com/nikolaspoczekaj/RefactorAI)