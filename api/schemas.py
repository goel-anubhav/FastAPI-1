import motor.motor_asyncio
from bson import objectid
from dotenv import load_dotenv
import os
load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URL"))

db = client.blog_api