# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
""" PostgreSQL adapter to connect to the database """
import psycopg2
from connectors.load_credentials import load_credentials

def init_postgre_connection():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # db credentials
        credentials = load_credentials()

        # connect to the PostgreSQL database
        print('Connecting to the PostgreSQL database ...')
        conn = psycopg2.connect(**credentials)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        raise ValueError(error)
