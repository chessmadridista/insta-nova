import requests
import logging
from .exceptions import (
    CredentialError, 
    AuthCodeMissingError,
    IncorrectAuthCodeError,
    ExpiredAuthCodeError,
    AuthCodeAlreadyUsedError,
)

logger = logging.getLogger(__name__)

class CredentialError(Exception):
    pass

class Client:
    """
    Instagram Client for interacting with the Instagram Graph API v23.0.

    # How to use it?
    ```
    from insta_nova.client import Client

    Client.app_id = "your-app-id"
    Client.app_secret = "your-app-secret"

    client = Client()
    ```
    This way, you will not need to define the app id
    and app secret every time you import the `Client` class in different modules.
    """
    _app_id = None
    _app_secret = None
    _INSTAGRAM_GRAPH_API_BASE_URL = "https://graph.instagram.com/v23.0/"
    
    def __init__(self, access_token=None):
        self.access_token = access_token

    def get_access_token(self, authorization_code):
        """
        Get the Instagram access token for the user.

        Args:
            authorization_code: The authorization code that is received after the user allows
                                access to his/her Instagram account.
        
        Raises:
            AuthCodeMissingError: If the auth code is not present.
            IncorrectAuthCodeError: If the auth code is incorrect.
            ExpiredAuthCodeError: If the auth code has expired.
            AuthCodeAlreadyUsedError: If the auth code has already been used in a prior request.
        """
        if not isinstance(authorization_code, str):
            raise AuthCodeMissingError
        
        if not authorization_code.strip():
            raise EmptyAuthCodeError
        INSTAGRAM_ACCESS_TOKEN_URL = "https://api.instagram.com/oauth/access_token"
        REDIRECT_URI = "https://localhost:5173/verify-instagram-account-connection-code"
        data = {
            'client_id': self.app_id,
            'client_secret': insta_app_client_secret,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': authorization_code
        }
    
        return "Some value"
    
    @classmethod
    def set_app_creds(cls, app_id: str, app_secret: str) -> None:
        """
        Set the application credentials for interacting with the Instagram Graph API.

        Args:
            app_id (str): The application ID.
            app_secret (str): The application secret key.

        Raises:
            CredentialError: If app_id or app_secret is not a string.
        """
        
        if not isinstance(app_id, str):
            raise CredentialError("app_id must be a string")
        if not isinstance(app_secret, str):
            raise CredentialError("app_secret must be a string")
        
        if not app_id.strip():
            raise CredentialError("app_id cannot be empty or whitespace-only")
        if not app_secret.strip():
            raise CredentialError("app_secret cannot be empty or whitespace-only")

        cls._app_id = app_id
        cls._app_secret = app_secret