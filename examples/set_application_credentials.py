"""
Example: Setting Up Application Credentials

This example demonstrates how to properly set up your Instagram Graph API
application credentials using the insta_nova library.

Prerequisites:
- Instagram Developer Account (https://developers.facebook.com/)
- Created Instagram App with App ID and App Secret

Security Note:
- Never hardcode credentials in production code
- Use environment variables or secure credential management
- Keep your app secret confidential

"""
import os
from insta_nova.client import Client

app_id = os.getenv("APP_ID")
app_secret = os.getenv("APP_SECRET")
Client.set_application_credentials(app_id=app_id, app_secret=app_secret) # Define this only once in your application.
client = Client() # After setting application credentials, you can use it in any module of your application.
