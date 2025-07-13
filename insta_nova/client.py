import requests
import logging
from .decorators import (
    validate_set_application_credentials,
    validate_get_access_token,
)

class Client:
    """
    Instagram Client for interacting with the Instagram Graph API v23.0.

    # How to use it?
    ```
    from insta_nova.client import Client

    app_id = "your-app-id"
    app_secret = "your-app-secret"
    Client.set_application_credentials(app_id=app_id, app_secret=app_secret)
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
    
    @classmethod
    @validate_set_application_credentials
    def set_application_credentials(cls, app_id: str, app_secret: str) -> None:
        """
        Set the application credentials for interacting with the Instagram Graph API.

        Args:
            app_id (str): The application ID.
            app_secret (str): The application secret key.

        Raises:
            CredentialError: If app_id or app_secret is not a string.
        """
        cls._app_id = app_id
        cls._app_secret = app_secret

    @validate_get_access_token
    def get_access_token(self, authorization_code: str, redirect_uri: str) -> dict:
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
        INSTAGRAM_ACCESS_TOKEN_URL = "https://api.instagram.com/oauth/access_token"
        payload = {
            'client_id': self._app_id,
            'client_secret': self._app_secret,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': authorization_code,
        }

        try:
            response = requests.post(INSTAGRAM_ACCESS_TOKEN_URL, payload)
            if response.status_code == 200:
                result = response.json()
                return result
            elif response.status_code == 400:
                raise Exception
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to Instagram API: {e}")
        