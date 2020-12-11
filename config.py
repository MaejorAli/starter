import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'alishaibu1234server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'alishaibu1234database'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'maejorali'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Aliali@17021986'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'alisahibu1234storage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '2XqYR15b00j/qI+nvw5H41yRDntXV4FrKiLU+RbmJyJ91uDXLc0392SodVCSZTt3V+N1Owipzow602xDH5RzWw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
