import requests
from .decorators import (
    validate_set_application_credentials,
    validate_get_access_token,
    validate_create_image_container,
    validate_publish_image_container,
)
from typing import Any

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
    _INSTAGRAM_GRAPH_API_BASE_URL = "https://graph.instagram.com/v23.0"
    
    def __init__(self, access_token: str | None = None):
        self._access_token = access_token
    
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
    def get_access_token(self, authorization_code: str, redirect_uri: str) -> dict[str, Any]:
        """
        Get the Instagram access token for the user.

        Args:
            authorization_code: The authorization code that is received after the user allows
                                access to his/her Instagram account.
            redirect_uri: The redirect URI that is mentioned in the Insta developer settings.
        
        Raises:
            AuthCodeMissingError: If the auth code is not present.
            IncorrectAuthCodeError: If the auth code is incorrect.
            ExpiredAuthCodeError: If the auth code has expired.
            AuthCodeAlreadyUsedError: If the auth code has already been used in a prior request.
        """
        INSTAGRAM_ACCESS_TOKEN_URL = "https://api.instagram.com/oauth/access_token"
        payload: dict[str, Any] = {
            'client_id': self._app_id,
            'client_secret': self._app_secret,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': authorization_code,
        }

        try:
            response = requests.post(INSTAGRAM_ACCESS_TOKEN_URL, data=payload)
            response_body = response.json()

            if response.status_code == 200:
                return response_body
            elif response.status_code == 400:
                raise Exception(f"Instagram API error: {response_body}")
            else:
                raise Exception(f"Unexpected status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to Instagram API: {e}")
    
    @validate_create_image_container
    def create_image_container(self, instagram_user_id: str, image_url: str) -> str:
        """
        Create container for the image that you want to publish on Instagram.

        Args:
            instagram_user_id (str): The id associated with the Instagram account which
                will be used to post the photo.
            image_url (str): The url of the image that needs to be posted on Instagram.
        
        Returns:
            container_id (str): The id of the created container if successful.
        """
        END_POINT = f'/{instagram_user_id}/media'
        URL = self._INSTAGRAM_GRAPH_API_BASE_URL + END_POINT
        payload: dict[str, Any] = {
            "access_token": self._access_token,
            "image_url": image_url,
        }

        try:
            response = requests.post(URL, data=payload)

            if response.status_code == 200:
                container_id = response.json()["id"]
                return container_id
            else:
                response_body = response.json()
                raise Exception(f"Instagram API error: {response_body}")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to Instagram API: {e}")
    
    @validate_publish_image_container
    def publish_image_container(self, instagram_user_id: str, container_id: str) -> str:
        """
        Publish the image container to Instagram to post your photo. The image will be posted
        on Instagram if this function executes successfully.

        Args:
            instagram_user_id (str): The id associated with the Instagram account which
                will be used to post the photo.
            container_id (str): The container id associated with the image to be published.

        Returns:
            media_id (str): The id of the published media.
        """
        _INSTAGRAM_GRAPH_API_BASE_URL = "https://graph.instagram.com/v23.0"
        END_POINT = f'/{instagram_user_id}/media_publish'
        URL = _INSTAGRAM_GRAPH_API_BASE_URL + END_POINT
        payload: dict[str, Any] = {
            "creation_id": container_id,
            "access_token": self._access_token,
        }
        
        try:
            response = requests.post(URL, data=payload)

            if response.status_code == 200:
                media_id = response.json()["id"]
                return media_id
            elif response.status_code == 400:
                response_body = response.json()
                raise Exception(f"Instagram API error: {response_body}")
            else:
                response_body = response.json()
                raise Exception(f"Instagram API error: {response_body}")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to Instagram API: {e}")
    
    def create_and_publish_image_container(self, instagram_user_id: str, image_url: str) -> str:
        """
        Creates and publishes the image container on Instagram.
        
        Note: This function is not stable. If the publish_image_container function fails then
            the call to the Instagram Graph API would have been wasted. Please use the separate
            functions create_image_container and publish_image_container in a sequential manner to avoid
            this issue.

        Args:
            instagram_user_id (str): The id associated with the Instagram account which
                will be used to post the photo.
            image_url (str): The url of the image that needs to be posted on Instagram.

        Returns:
            media_id (str): The id associated with the published media after it has been 
                published successfully. 
        """
        container_id = self.create_image_container(instagram_user_id, image_url)
        media_id = self.publish_image_container(instagram_user_id, container_id)
        return media_id