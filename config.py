import os
from dotenv import load_ditenv

load_dotenv()

#read configuration
BASE_URL=os.getenv("BASE_URL")
VALID_USERNAME=os.getenv("VALID_USERNAME")"
VALID_PASSWORD=os.getenv("VALID_PASSWORD")

#variabled required configuration
required_variables = {
    "BASE_URL": BASE_URL,
    "VALID_USERNAME":VALID_USERNAME,
    "VALID_PASSWORD":VALID_PASSWORD
}