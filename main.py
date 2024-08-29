# provides ways to access the Operating System and allows us to read the environment variables
import os

from src.extract import create_and_extract_data
from src.transform import transform_and_remove_duplicate
from src.extract import connect_to_postgress
from src.update import update_values

from dotenv import load_dotenv
load_dotenv() #take environment variables from .env only for local testing

#import environment variables from .env file
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")

#this creates a variable that the script execution start time
start_time = datetime.now()

# make a connection to postgres and insert data from csv file in local env
print("\nExtracting and transforming data in sql...")
create_and_extract_data(dbname, host, port, user, password)
print('\nExtraction and transformation in sql completed')

# remove duplicated data and removing unneeded column
print("\nRemoving duplicated data...")
transform_and_remove_duplicate(dbname, host, port, user, password)
print('\nDuplicated data removed')

# this creates a variable that calculates how long it takes to run the script
execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")
#extract and transfroming data will be done in postgresql so we just call the function

#to remove unneeded column and duplicate
#transform_and_remove_duplicate()


