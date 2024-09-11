import psycopg2

#PostgresSQL connection properties
def connect_to_postgres( dbname, user, password, host, port):
    conn = psycopg2.connect(
        dbname = dbname,
        user = user,
        password = password,
        host = host,
        port = port
        ) 
    
    return conn

def create_and_extract_data(dbname, user, password, host, port):
    
    conn = connect_to_postgres(dbname, user, password, host, port)
    cursor = conn.cursor()

    #Create a table first as we are using psycopg2 copy method
    cursor.execute ('CREATE TABLE fuelprice (dt_type Varchar, date date, ron95 decimal, ron97 decimal, diesel decimal, diesel_eastmsia decimal);')

    #URL of the parquet file
    URL_DATA = 'https://storage.data.gov.my/commodities/fuelprice.parquet'

    #Fetch the parquet file from the API
    response = requests.get(URL_DATA)
    if response.status_code == 200:
        print("Successfully fetched data from API.")
    else:
        print(f"Error fetching data: {response.status_code}")
        raise Exception("Failed to download parquet file.")

    #Load the parquet file into a pandas DataFrame
    df = pd.read_parquet(io.BytesIO(response.content))

    #Convert DataFrame to CSV format in memory
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)

    #Move the buffer cursor to the start
    csv_buffer.seek(0)

    #Use `cursor.copy_expert` to load data from CSV-like buffer into PostgreSQL
    try:
        cursor.copy_expert(
            "COPY fuelprice (dt_type, date, ron95, ron97, diesel, diesel_eastmsia) FROM STDIN WITH CSV HEADER", 
            csv_buffer
        )
        conn.commit()  # Commit the transaction
        print("Data successfully inserted into PostgreSQL.")
    except Exception as e:
        conn.rollback()  # Rollback on error
        print(f"Error during database operation: {e}")
    finally:
        cursor.close()
        conn.close()  # Close the connection
