import psycopg2
from psycopg2 import Error, connect

try:
    connection = psycopg2.connect(
        user = 'postgres',
        password = '14xs97akz7z',
        host = 'localhost',
        port = '5432',
        database = 'computer'
    )
    cursor = connection.cursor()
    # cursor.execute("UPDATE PC SET model = 'ASUS' WHERE ram = 16;")
    # connection.commit()
    id = int(input('ENTER id '))
    screen = int(input('ENTER screen '))
    model = input('ENTER model ')
    speed = int(input('ENTER speed '))
    ram = int(input('ENTER ram '))
    massa = int(input('ENTER massa '))

    cursor.execute(f"INSERT INTO LAPTOP(id,screen,model,speed,ram,massa) \
            VALUES({id},{screen},'{model}',{speed},{ram},{massa})") 
    connection.commit()   
        

except (Exception, Error) as error:
    print('Error is ', error)
finally:
    if connection:
        connection.close()
        cursor.close()
        print('PostgresSQL is closed')