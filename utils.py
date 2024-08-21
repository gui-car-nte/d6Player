from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = MongoClient(os.getenv('DB_URI'))
    database = client['D6Player']
    
except Exception as ex:
    print("Error connecting to the server: {}".format(ex))
finally:
    client.close()
    print("Connection ended")