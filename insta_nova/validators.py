"""
This file contains validation functions to check the quality of function arguments
before sending a request to the Instagram API.
"""
from urllib.parse import urlparse
from .exceptions import (
    CredentialTypeError, 
    CredentialValueError,
    AuthorizationCodeTypeError,
    AuthorizationCodeValueError,
    RedirectUriTypeError,
    RedirectUriValueError,
    RedirectUriFormatError,
    InstagramUserIdTypeError,
    InstagramUserIdValueError,
    ContainerIdTypeError,
    ContainerIdValueError,
)
from typing import Type

def _validate_non_empty_string(
    value: str,
    field_name: str,
    type_error: Type[TypeError],
    value_error: Type[ValueError]
) -> None:
    if not isinstance(value, str):  # type: ignore[arg-type]
        raise type_error(f"{field_name} must be a string")
    if not value.strip():
        raise value_error(f"{field_name} cannot be empty or whitespace-only")

def _validate_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def validate_app_id(app_id: str) -> None:
    _validate_non_empty_string(app_id, "app_id", CredentialTypeError, CredentialValueError)

def validate_app_secret(app_secret: str) -> None:
    _validate_non_empty_string(app_secret, "app_secret", CredentialTypeError, CredentialValueError)

def validate_authorization_code(authorization_code: str) -> None:
        _validate_non_empty_string(authorization_code, "authorization_code", AuthorizationCodeTypeError, AuthorizationCodeValueError)

def validate_redirect_uri(redirect_uri: str) -> None:
    _validate_non_empty_string(redirect_uri, "redirect_uri", RedirectUriTypeError, RedirectUriValueError)

    is_redirect_uri_valid = _validate_url(redirect_uri)
    if not is_redirect_uri_valid:
        raise RedirectUriFormatError("redirect_uri is an invalid uri")

def validate_instagram_user_id(instagram_user_id: str) -> None:
    _validate_non_empty_string(instagram_user_id, "instagram_user_id", InstagramUserIdTypeError, InstagramUserIdValueError)

def validate_container_id(container_id: str) -> None:
    _validate_non_empty_string(container_id, "container_id", ContainerIdTypeError, ContainerIdValueError)