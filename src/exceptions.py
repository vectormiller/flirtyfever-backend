"""
    Exception types for custom exceptions.
"""

class ExceptionWithMessage(Exception):
    """
    Exception class that includes a custom message.
    
    This exception can be raised when you need to provide a specific error message along with the exception.

    Attributes:
        message (str): The custom error message associated with the exception.

    Args:
        message (str): The custom error message to be included in the exception.

    Example:
        try:
            something()
        except Exception:
            raise ExceptionWithMessage("Unexpected behavior occurred, REF: #124")
        
        Output: ExceptionWithMessage: Unexpected behavior occurred, REF: #124
    """
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(*args)
        self.message = message

    def __str__(self) -> str:
        return str(self.message)


class EnvVarLoadingException(Exception):
    """
    Exception class for environment variable loading errors.

    This exception can be raised when there is an issue related to loading environment variables.

    Args:
        *args: Additional arguments to pass to the base Exception class.

    Example:
        try:
            settings = load_settings()
        except Exception as e:
            raise EnvVarLoadingException(e) from e

        Output: EnvVarLoadingException: Failed to load environment variable
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
