""" Small script that allows you to insert the data from the API to postgres """
import requests
from connectors.postgress_connector import init_postgre_connection

connection = init_postgre_connection()

def run():
    """ Runner, executes the sql files, gets data from api and inserts into postgres """
    api_data = get_data()
    sql_files = ['users.sql']
    execute(sql_files)
    insert('USERS', api_data)

def get_data():
    """ Gets the data from the Rest API """
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    return response.json()

def execute(filenames):
    """ Executes the sql files names to create the tables """
    with connection.cursor() as cursor:
        for file in filenames:
            cursor.execute(open(file, 'r').read())
        connection.commit()

def insert(tablename, data):
    """ Inserts values into database from the API """
    with connection.cursor() as cursor:
        for item in data:
            query = '''INSERT INTO {} VALUES (%s, %s, %s, %s)'''.format(tablename)
            cursor.execute(query, list(item.values()))
            connection.commit()

if __name__ == "__main__":
    run()