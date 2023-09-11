class ExceptionWithMessage(Exception):
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(*args)
        self.message = message

    def __str__(self) -> str:
        return str(self.message)


class EnvVarLoadingException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)