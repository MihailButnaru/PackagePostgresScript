# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import os
import json
from connectors.postgress_connector import init_postgre_connection

class SQLManager():

    def __init__(self, filenames):
        self._filenames = filenames
        self._connection = init_postgre_connection()

    def execute_sql_files(self):
        """ Executes the sql file names to create the tables """
        with self._connection.cursor() as cursor:
            for file in self._filenames:
                cursor.execute(open(file, 'r').read())
            self._connection.commit() # commit the changes

    def insert(self, tablename, json_data):
        """ Inserts values into database from the API """
        with self._connection.cursor() as cursor:
            for item in json_data:
                query = '''INSERT INTO {} VALUES (%s, %s, %s, %s) '''.format(tablename)
                cursor.execute(query, list(item.values()))
                self._connection.commit()

    def delete(self, tablename):
        """ Deletes the table """
        with self._connection.cursor() as cursor:
            query = '''DROP TABLE IF EXISTS {} '''.format(tablename)
            cursor.execute(query)
            self._connection.commit()