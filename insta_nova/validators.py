"""
This file contains validation functions to check the quality of function arguments
before sending a request to the Instagram API.
"""
from urllib.parse import urlparse
from .exceptions import (
    CredentialError, 
    AuthCodeMissingError,
    IncorrectAuthCodeError,
    ExpiredAuthCodeError,
    AuthCodeAlreadyUsedError,
    EmptyAuthCodeError,
    AuthorizationCodeTypeError,
    RedirectUriTypeError,
    InstagramUserIdTypeError,
)

def _validate_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def validate_app_id(app_id: str) -> None:
    if not isinstance(app_id, str): # type: ignore[arg-type]
        raise CredentialError("app_id must be a string")
    if not app_id.strip():
        raise CredentialError("app_id cannot be empty or whitespace-only")

def validate_app_secret(app_secret: str) -> None:
    if not isinstance(app_secret, str):
        raise CredentialError("app_secret must be a string")
    if not app_secret.strip():
        raise CredentialError("app_secret cannot be empty or whitespace-only")

def validate_authorization_code(authorization_code: str) -> None:
    if not isinstance(authorization_code, str):
        raise AuthorizationCodeTypeError("redirect_uri must be a string")    

def validate_redirect_uri(redirect_uri: str) -> None:
    if not isinstance(redirect_uri, str):
        raise RedirectUriTypeError("redirect_uri must be a string")
    if not redirect_uri.strip():
        raise RedirectUriValueError("redirect_uri cannot be empty or whitespace-only")

    is_redirect_uri_valid = _validate_url(redirect_uri)
    if not is_redirect_uri_valid:
        raise RedirectUriFormatError("redirect_uri is an invalid uri")

def validate_instagram_user_id(instagram_user_id: str) -> None:
    if not isinstance(instagram_user_id, str):
        raise InstagramUserIdTypeError("instagram_user_id must be a string")
    if not instagram_user_id.strip():
        raise InstagramUserId("redirect_uri cannot be empty or whitespace-only")

def validate_container_id(container_id: str) -> None:
    if not isinstance(container_id, str):
        raise InstagramUserIdTypeError("instagram_user_id must be a string")
    if not container_id.strip():
        raise RedirectUriValueError("redirect_uri cannot be empty or whitespace-only")