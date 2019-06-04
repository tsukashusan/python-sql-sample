#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyodbc

server = '<server>'
database = '<database>'
username = '<username>'
password = '<password>'
driver= 'SQL Server Native Client 11.0'
port=<portnumber>

connection_string = " DRIVER={%s};SERVER=%s;PORT=%d;DATABASE=%s;UID=%s;PWD=%s;PORT=%d" \
                     % (driver, server, port, database, username, password, port)


print(connection_string)
pyodbc.pooling = True


with pyodbc.connect(connection_string) as conn:
    #conn = pymssql.connect(server=server, user=username, password=password, database=database)  
    with conn.cursor() as cursor:  
        cursor.execute('SELECT 1')  
        row = cursor.fetchone()  
        while row:
            print(row[0])
            row = cursor.fetchone()

exit(0)