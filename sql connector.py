import mysql.connector
from mysql.connector import Error
import pandas as pd
def sqlconnector(host_name, username, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name, user=username, password=user_password, auth_plugin='mysql_native_password')
        print('MySQl database connection successful')
    except Error as e:
        print(e)
    return connection

    
sqlconnector('localhost', 'root', 'root123')