from functools import wraps
from .validators import (
    validate_app_id,
    validate_app_secret,
    validate_authorization_code,
    validate_redirect_uri,
    validate_instagram_user_id,
    validate_container_id,
)
from typing import Callable, Any

def validate_set_application_credentials(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(cls: type[Any], app_id: str, app_secret: str) -> Callable[..., Any]:
        validate_app_id(app_id)
        validate_app_secret(app_secret)
        return func(cls, app_id, app_secret)
    return wrapper

def validate_get_access_token(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(self: object, authorization_code: str, redirect_uri: str) -> Callable[..., Any]:
        validate_authorization_code(authorization_code)
        validate_redirect_uri(redirect_uri)
        return func(self, authorization_code, redirect_uri)
    return wrapper

def validate_create_image_container(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(self: object, app_id: str, app_secret: str) -> Callable[..., Any]:
        validate_app_id(app_id)
        validate_app_secret(app_secret)
        return func(self, app_id, app_secret)
    return wrapper

def validate_publish_image_container(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(self: object, instagram_user_id: str, container_id: str) -> Callable[..., Any]:
        validate_instagram_user_id(instagram_user_id)
        validate_container_id(container_id)
        return func(self, instagram_user_id, container_id)
    return wrapper