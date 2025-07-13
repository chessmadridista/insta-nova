from functools import wraps
from .validators import (
    validate_app_id,
    validate_app_secret,
    validate_authorization_code,
    validate_redirect_uri,
)

def validate_set_application_credentials(func):
    @wraps(func)
    def wrapper(cls, app_id, app_secret):
        validate_app_id(app_id)
        validate_app_secret(app_secret)
        return func(cls, app_id, app_secret)
    return wrapper

def validate_get_access_token(func):
    @wraps(func)
    def wrapper(self, authorization_code, redirect_uri):
        validate_authorization_code(authorization_code)
        validate_redirect_uri(redirect_uri)
        return func(self, authorization_code, redirect_uri)
    return wrapper

