from datetime import datetime
from enum import Enum
from typing import Optional

class LogLevel(Enum):
    INFO = 'info'
    
class LoggerService:
    """A fake exernal logging service (to be mocked in test)."""
    def __init__(self, name: str = "Logger", level: LogLevel = LogLevel.INFO ):
        self.name = name
        self.level = level

    def _get_timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self, level: Optional[LogLevel] = None, message: str):
        """"""
        if self.level not in LogLevel or level not in LogLevel:
            raise ValueError(f"Invalid log level: {level}")
        
        print(f"[{self._get_timestamp()}] [{self.name or level }] [{self.level}] {message}")
