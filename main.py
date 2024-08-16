# provides ways to access the Operating System and allows us to read the environment variables
import os

from src.extract import create_and_extract_data
from src.transform import transform_and_remove_duplicate

from dotenv import load_dotenv
load_dotenv() #take environment variables from .env only for local testing

#import environment variables from .env file
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")

#extract and transfroming data will be done in postgresql so we just call the function

create_and_extract_data()

transform_and_remove_duplicate()

