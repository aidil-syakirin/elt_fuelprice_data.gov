from airflow.decorators import dag, task
from airflow.hooks.postgres_hook import PostgresHook
from datetime import datetime
import pendulum
import pandas as pd
import os

@dag(
    start_date=pendulum.datetime(2024,9,9),
    schedule="5 0 * * 4", #Run every thursday at 0005 hrs
    catchup=False,
    max_active_runs=1
)
def fuelprice_etl():
    @task()
    def extract_data():
        # Print message, return a response
        print("Extracting data from fuel price API")

        URL_DATA = 'https://storage.data.gov.my/commodities/fuelprice.parquet'

        df = pd.read_parquet(URL_DATA)
        if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])

        #Pick the data for this week and series_type = level 
        thisweek = pendulum.now()
        thisweek = thisweek.subtract(days=7).format('YYYY-MM-DD')

        tr_df = df[df['series_type'] == 'level'][df['date'] > thisweek]

        return tr_df

    @task()
    def transform_data(tr_df):
        
        #Transform the update by dropping the series_type column to match the existing table 
        tr_df = tr_df.drop('series_type',axis=1)
      
        return tr_df

    @task
    def load_data(tr_df):
        try:
            # Use Airflow's PostgresHook to get the connection
            hook = PostgresHook(postgres_conn_id = "postgres_default")
            
            # Get SQLAlchemy engine from the connection
            engine = hook.get_sqlalchemy_engine()

            # Load the DataFrame into the 'test_fuelprice' table in Postgres
            tr_df.to_sql('tr_fuelprice', engine, if_exists='append', index=False)
            print("The dataframe is inserted")
        except Exception as error:
            print(f"Error: {error}")
        finally:
            engine.dispose()  # Close the connection


    # Set dependencies using function calls
    tr_df = extract_data()
    transformed_dataset = transform_data(tr_df)
    load_data(transformed_dataset)


# Allow the DAG to be run
fuelprice_etl()
