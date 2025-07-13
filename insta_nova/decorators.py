from functools import wraps
from .validators import (
    validate_app_id,
    validate_app_secret,
)

def validate_set_application_credentials(func):
    @wraps(func)
    def wrapper(cls, app_id, app_secret):
        validate_app_id(app_id)
        validate_app_secret(app_secret)
        return func(cls, app_id, app_secret)
    return wrapper
