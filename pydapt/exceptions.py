class InvalidArgumentException(Exception):
    """
    Custom Exception raised arguments supplied to constructor are invalid
    """
    def __init__(self, message):
        self.message = message
