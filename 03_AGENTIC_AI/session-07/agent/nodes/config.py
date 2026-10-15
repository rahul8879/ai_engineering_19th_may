# import all the libraries
import os
import secrets
from dotenv import load_dotenv

print(load_dotenv()) # load all the credentials from .env file

# I am taking only one email for now( because I dont have access of entire worksations access)
ORGANIZER_EMAIL = "rtiwarirahul123@gmail.com"
ALLOW_DUPLICATE_EVENTS = os.environ.get("ALLOW_DUPLICATE_EVENTS", "false").lower() == "true"

DATA_DIR = os.path.join("data")
RUN_STORE_DB_PATH = os.environ.get("RUN_STORE_DB_PATH", os.path.join(DATA_DIR, "runs.db"))
CHECKPOINT_DB_PATH = os.environ.get("CHECKPOINT_DB_PATH", os.path.join(DATA_DIR, "checkpoints.db"))

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALENDAR_CREDENTIALS_PATH = os.path.join(
    PROJECT_ROOT, "calendar-server", "gcp-oauth.keys.json"
)


MCP_SERVERS = {
    "ats": {
        "command": "python",
        "args": [os.path.join( "server", "server.py")],
        "transport": "stdio",
    },
    "calendar": {
        "command": "npx",
        "args": ["@cocal/google-calendar-mcp"],
        "transport": "stdio",
        "env": {"GOOGLE_OAUTH_CREDENTIALS": CALENDAR_CREDENTIALS_PATH, **os.environ},
    },
    "email": {
        "command": "npx",
        "args": ["@gongrzhe/server-gmail-autoauth-mcp"],
        "transport": "stdio",
    },
}



