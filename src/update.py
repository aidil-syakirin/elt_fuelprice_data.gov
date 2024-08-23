
#fetch update data from dat.gov 
import pandas as pd

URL_DATA = 'https://storage.data.gov.my/commodities/fuelprice.parquet'

df = pd.read_parquet(URL_DATA)
if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])

#Pick the data after 08/08/2024 (last update) and series_type = level 

tr_df = df[df['series_type'] == 'level'][df['date'] > '2024-08-08']

#Transform the update by dropping the series_type column to match the existing table 
tr_df = tr_df.drop('series_type',axis=1)


#Append the new data into existing table by using psycopg2. Need to change the dataframe into tuple first
import psycopg2 
import numpy as np 
import psycopg2.extras as extras 
from src import connect_to_postgress()


def execute_values(conn, df, table): 

	tuples = [tuple(x) for x in df.to_numpy()] 

	cols = ','.join(list(df.columns)) 
	# SQL query to execute 
	query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols) 
	cursor = conn.cursor() 
	try: 
		extras.execute_values(cursor, query, tuples) 
		conn.commit() 
	except (Exception, psycopg2.DatabaseError) as error: 
		print("Error: %s" % error) 
		conn.rollback() 
		cursor.close() 
		return 1
	print("the dataframe is inserted") 
	cursor.close() 


conn = connect_to_postgress(dbname, user, password, host, port)

execute_values(conn, tr_df, 'tr_fuelprice') 
