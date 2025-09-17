from datetime import datetime
from enum import Enum
from typing import Optional
    
class LogLevel(Enum):
    INFO = 'info'
    DEBUG = "debug"
    WARNING = "warning"
    ERROR = "error"
        

class LoggerService:
    """A fake exernal logging service (to be mocked in test)."""
    def __init__(self, name: str = "Logger", level: LogLevel = LogLevel.INFO ):
        self.name = name
        self.level = level

    def _get_timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self,  message: str, level: Optional[LogLevel] = None):
        """"""
        active_level = level or self.level
        
        if not isinstance(active_level, LogLevel):
            raise ValueError(f"Invalid log level: {active_level}")
        
        print(f"[{self._get_timestamp()}] [{ self.name}] [{active_level.value.upper()}] {message}")
