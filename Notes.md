# Note
- This file is for brain dumping I will use it to work on planning, roadmap and everything else related to this library.
- If you have a feature to suggest or something related to this project, then please add a new issue and we will have a discussion there.

# Todo
- [ ] Add project setup instructions in README.md
- [ ] Improve the documentation of the project.

# GH-5
Okay, so the thing I can't wrap my head around is how do I use the Instagram Client? How do I import it?!
Just writing down the rough implementation here. So in app.py:
```
from insta_nova.client import Client

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")

Client(app_id=APP_ID, app_secret=APP_SECRET)
```
Since app id will be common across all the users that connect to this app, I need to set it in a config or something because access token of users will be different and I don't want to initialise this separately in every function that I use it in. It will become very bloated.