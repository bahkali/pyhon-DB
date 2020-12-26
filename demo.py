import psycopg2

connection = psycopg2.connect(  user="postgres", password="Jerico05", host="localhost", port="5433", database="test")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY, 
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')

connection.commit()
connection.close()
cursor.close()