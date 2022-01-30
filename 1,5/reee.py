import psycopg2
from psycopg2 import Error, connect






# conn = psycopg2.connect(
# user = 'postgres',
# password = '14xs97akz7z',
# host = 'localhost',
# port = '5432',
# database = 'computer'
#     )
# cur = conn.cursor()
# cur.execute('INSERT INTO laptop (id, screen, model, speed, ram, massa) VALUES (2, 10, 60, 20, 40, 23)')

# conn.commit()
# cur.close()
# conn.close()

# if conn.close:
#     print('Postgres connection closed')



connetion = psycopg2.connect(
    user = 'postgres',
    password = '14xs97akz7z',
    host = 'localhost',
    port = '5432',
    database = 'education'
)

cursor_1 = connetion.cursor()

name = input("Enter name: ")
# school_number = int(input('Enter school_number: '))
# cursor_1.execute('CREATE TABLE district( id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY, name VARCHAR)')
# cursor_1.execute('CREATE TABLE schools(id integer REFERENCES district(id), name varchar, school_number integer)')
cursor_1.execute("INSERT INTO district(name)  VALUES (%s)", f'({name})',) 
if cursor_1.execute:
    print('insert into district has done')
cursor_2 = connetion.cursor()
# cursor_1.execute('INSERT INTO schools(id, name, school_number) VALUES((%s), (%s), (%s))', ((3), 'Kerme - Too', (5)), )
# if cursor_2.execute:
#     print('Insert into schools has done')
connetion.commit()
connetion.close()
if connetion.close:
    print('connection closed')