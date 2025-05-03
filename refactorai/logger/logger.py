import logging
import sys

# ANSI-Farbcodes
COLORS = {
    'DEBUG': '\033[90m',      # Grau
    'INFO': '\033[36m',       # Cyan
    'SUCCESS': '\033[92m',    # Grün
    'WARNING': '\033[93m',    # Gelb
    'ERROR': '\033[91m',      # Rot
    'RESET': '\033[0m'
}

class ColorFormatter(logging.Formatter):
    def format(self, record):
        color = COLORS.get(record.levelname, COLORS['RESET'])
        msg = super().format(record)
        return f"{color}{msg}{COLORS['RESET']}"

class SuccessLogger(logging.Logger):
    SUCCESS = 25
    def success(self, msg, *args, **kwargs):
        if self.isEnabledFor(self.SUCCESS):
            self._log(self.SUCCESS, msg, args, **kwargs)

logging.setLoggerClass(SuccessLogger)
logging.addLevelName(25, "SUCCESS")

def setup_logging(level=logging.INFO):
    handler = logging.StreamHandler(sys.stdout)
    formatter = ColorFormatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger = logging.getLogger("global_logger")
    logger.setLevel(level)
    logger.handlers = [handler]
    return logger

logger = setup_logging()


