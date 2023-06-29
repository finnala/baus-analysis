from dotenv import load_dotenv
import os
from client import HTTPClient


load_dotenv()

API_KEY = os.environ.get("API_KEY")
client = HTTPClient(API_KEY)

