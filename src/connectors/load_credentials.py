""" Credentials Loader from a file """
from configparser import ConfigParser


def load_credentials(filename='credentials.ini', section='postgresql'):
    """ Loads the database credentials from the file """
    parser = ConfigParser() # create a parser
    parser.read(filename) # read config file

    database = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            database[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return database
