# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:09:00 2022

@author: 91777
"""

# Assignment 7:- Python Database Connection Project which updates any one value in the table and select all the table data and print it.

import mysql.connector as sql           

# Connecting the local mysql database
database = sql.connect(host = 'localhost', user = 'root', passwd = 'sqldatapass', database = 'Internet')

cur = database.cursor()


cur.execute("update Internet num = 80 where Roll_no = 122")     
cur.execute("select * from Name")

for i in cur:
    print(i)

cur.close()
database.commit()       
