
from extract import connect_to_postgres 

def transform_and_remove_duplicate(dbname, user, password, host, port):

    #postgresql configuration
    conn = connect_to_postgres(dbname, user, password, host, port)
    
    #open a connection sesion to sql 
    cursor = conn.cursor()

    #creating a table with level dt_types only as there is 2 data entry for specific date
    cursor.execute('''CREATE TABLE tr_fuelprice AS (SELECT * FROM fuelprice WHERE dt_type = 'level');''')

    #remove dt_type column as we no longer need for analysis
    cursor.execute('ALTER TABLE tr_fuelprice DROP COLUMN dt_type')
    conn.commit()
    cursor.close()
    
    return
