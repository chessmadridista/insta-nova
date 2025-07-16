class CredentialTypeError(TypeError):
    """Raised when credential parameter is not a string."""
    pass

class CredentialValueError(ValueError):
    """Raised when credential parameter is empty or whitespace-only."""
    pass

class AuthorizationCodeTypeError(TypeError):
    """Raised when authorization code parameter is not a string."""
    pass

class AuthorizationCodeValueError(ValueError):
    """Raised when authorization code parameter is empty or whitespace-only."""
    pass

class RedirectUriTypeError(TypeError):
    """Raised when redirect URI parameter is not a string."""
    pass

class RedirectUriValueError(ValueError):
    """Raised when redirect URI parameter is empty or whitespace-only."""
    pass

class RedirectUriFormatError(ValueError):
    """Raised when redirect URI parameter has an invalid format."""
    pass

class InstagramUserIdTypeError(TypeError):
    """Raised when Instagram user ID parameter is not a string."""
    pass

class InstagramUserIdValueError(ValueError):
    """Raised when Instagram user ID parameter is empty or whitespace-only."""
    pass

class ContainerIdTypeError(TypeError):
    """Raised when container ID parameter is not a string."""
    pass

class ContainerIdValueError(ValueError):
    """Raised when container ID parameter is empty or whitespace-only."""
    pass
