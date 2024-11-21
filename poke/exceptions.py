class PokeAPIError(Exception):
    """Base exception for all PokeAPI-related errors."""
    def __init__(self, message: str):
        super().__init__(f"PokeAPI Error: {message}")

class PokeAPINetworkError(PokeAPIError):
    """Raised when there's a network-related error."""
    def __init__(self, message: str):
        super().__init__(f"Network Error: {message}")

class PokeAPIResponseError(PokeAPIError):
    """Raised for invalid or unsuccessful responses from the API."""
    def __init__(self, status_code: int, message: str = "An error occurred"):
        super().__init__(f"API Response Error {status_code}: {message}")
