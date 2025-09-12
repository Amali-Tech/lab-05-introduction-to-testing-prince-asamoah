class LoggerService:
    """A fake exernal logging service (to be mocked in test)."""
    def log(self, message: str):
        print(f'[LOG]: {message}')