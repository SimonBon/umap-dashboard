class UnexpectedError(Exception):
    """Custom exception for a specific error in the application."""

    def __init__(self, message="Unexpected Error occured!"):
        self.message = message
        super().__init__(self.message)