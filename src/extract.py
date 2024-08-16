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

    #create a session with sql server
    cursor = conn.cursor()

    # create a table named fuel_price, define the column name
    cursor.execute ('CREATE TABLE fuelprice (dt_type Varchar, date date, ron95 decimal, ron97 decimal, diesel decimal, diesel_eastmsia decimal);')

    #extract the csv file into the created table
    with open(".....\fuelprice.csv", 'r') as f:
        cursor.copy_expert(f"COPY fuelprice (dt_type, date, ron95, ron97, diesel, diesel_eastmsia) FROM STDIN WITH CSV HEADER", f)

    # to commit the transaction
    conn.commit()

    #close session
    cursor.close()

    return