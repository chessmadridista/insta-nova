"""
Pytest configuration and shared fixtures for insta_nova tests.
"""
import pytest
import sys
import os

# Add the parent directory to Python path so we can import insta_nova
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture
def access_token():
    """Sample Instagram access token for testing."""
    return "IGQVJ123456789_sample_token"

@pytest.fixture
def client(access_token):
    """Create an Instagram client instance for testing."""
    from insta_nova.client import InstagramClient
    return InstagramClient(access_token)