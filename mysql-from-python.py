import os
import datetime
import pymysql
import json


# set mysql username
username = "poldi"
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='poldimysql',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        list_of_names = ['fred','Fred']
        # prepare a string with the same number of placeholders
        format_strings = ','.join(['%s']*len(list_of_names)) 
        cursor.execute("DELETE FROM Friends WHERE name in ({0});".format(format_strings), list_of_names)
        connection.commit()  

finally:
    # close the connection, regardless of whether the above was successful
    connection.close()

