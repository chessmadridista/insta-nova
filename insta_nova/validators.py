"""
This file contains validation functions to check the quality of function arguments
before sending a request to the Instagram API.
"""
from urllib.parse import urlparse
from .exceptions import (
    CredentialTypeError, 
    CredentialValueError,
    AuthorizationCodeTypeError,
    RedirectUriTypeError,
    InstagramUserIdTypeError,
)
from typing import Type

def _validate_non_empty_string(
    value: str,
    field_name: str,
    type_error: Type[Exception],
    value_error: Type[Exception]
) -> None:
    if not isinstance(value, str):  # type: ignore[arg-type]
        raise type_error(f"{field_name} must be a string")
    if not value.strip():
        raise value_error(f"{field_name} cannot be empty or whitespace-only")

def _validate_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def validate_app_id(app_id: str) -> None:
    _validate_non_empty_string(app_id, "app_id", CredentialTypeError, CredentialValueError)

def validate_app_secret(app_secret: str) -> None:
    _validate_non_empty_string(app_secret, "app_secret", CredentialTypeError, CredentialValueError)

def validate_authorization_code(authorization_code: str) -> None:
    if not isinstance(authorization_code, str):
        raise AuthorizationCodeTypeError("redirect_uri must be a string")    
    _validate_non_empty_string(app_secret, "app_secret", CredentialError)

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