# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from connectors.postgress_connector import init_postgre_connection
from sql.sql_manager import SQLManager
from core.api_manager import APIManager

if __name__ == "__main__":
    # list of sql file names to be executed
    sql_files = ['users.sql']
    # sql manager
    sql_manager = SQLManager(sql_files) # list of file names required

    # used to execute sql files
    # sql_manager.execute_sql_files() 

    endpoint = 'https://jsonplaceholder.typicode.com/todos'
    api_manager = APIManager(endpoint)

    # Get data from the API
    # sql_manager.insert('USERS', api_manager.get())

    # Delete table
    # sql_manager.delete('USERS')