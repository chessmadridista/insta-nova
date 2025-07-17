import pytest
import responses
from insta_nova.client import Client

@responses.activate
def test_get_access_token_success(client):
    """Test successful access token retrieval."""
    mock_response = {
        "access_token": 'IGQUI_sample_123',
        "user_id": '1235753245'
    }
    responses.add(responses.GET, "https://graph.instagram.com/v23.0/me", json=mock_response, status=200)
    result = client.get_access_token()

    assert result["access_token"] == "IGQUI_sample_123"
    assert result["user_id"] == "1235753245"