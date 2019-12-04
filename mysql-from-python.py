import os
import pymysql

# set mysql username
username = "poldi"
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='poldimysql',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    # close the connection, regardless of whether the above was successful
    connection.close()
    
