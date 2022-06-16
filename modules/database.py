"""
1) Database server --> Mysql

db example:
$ create database april2022

-- DDl
-- create table in april2022 db

$ create table student(
	id int,
    name varchar(100),
    location varchar(60)
)

# DML(insert, update, read, delete)

# how to read data from table

-- select id, name from student
select * from student

# how to insert the data into table

-- insert into student(id, name, location) values(3, 'vinay1', 'bangalore');


# how to update the data in table
-- update  student set name='moinika' where id=1
-- update student set location='pune' where id=3

# how to delete the rows in table
delete from student where name='vinay'
--------------------------------------------------



database server
  --> databasename1
       --> tables
  --> databsenames2
       --> tables



referene:
 https://www.sqlshack.com/how-to-install-mysql-database-server-8-0-19-on-windows-10/

step #1 : install mysql server on your machine


mysql : 3306
33060
root user details : Sumanit@123

badra/Sumanit@123

# create new database in mysql server

create database demodb

# create table in database 'demodb'

CREATE TABLE testtable(
name varchar(10),
age int
)


# edit preference --> Sql Edittor  --> uncheck 'TO safe update'


# steps to connect with mysql db from python:

step #1: Install mysql module

 # you get errors if c is not available in your machine
 $ pip install mysqlclient


 # refere for alternate installtion
 https://www.a2hosting.in/kb/developer-corner/mysql/connecting-to-mysql-using-python

step #1:
 import mysql module

# use methods in that module



virtualenv sqldbenv


"""
# db connection details
hostname = '127.0.0.1'
username = 'badra'
password = 'Sumanit@123'
database = 'demodb'

import MySQLdb


# connect with db
myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)

#print(myConnection)
#cur = myConnection.cursor()
#
# # fecth all records
#cur.execute("SELECT * FROM dept")
#for dept in cur.fetchall():
#    print(dept[-1])
# #print(cur.fetchall())

# lets insert records into db

db_cursor = myConnection.cursor()

sql_statement = """
INSERT INTO 
dept(dept_id, department_name, description, location)
VALUES
(10,
'test dept name',
'test description',
'hyd');
"""
#db_cursor.execute(sql_statement)
#db_cursor.connection.commit()


# update records in db
update_query = "update dept set department_name='{dept_name}' where dept_id={dept_id}"

query_with_values = update_query.format(dept_name='ABCD', dept_id=10)
print(query_with_values)
#db_cursor.execute(query_with_values)
#db_cursor.connection.commit()

# read
# insert
# update

# delete the data

delete_query = "DELETE from dept where dept_id={dept_id}"

del_query = delete_query.format(dept_id=15)
#db_cursor.execute(del_query)
#db_cursor.connection.commit()
#print(db_cursor.rowcount)



read_query = "SELECT * FROM dept where dept_id={dept_id}"
r_query = read_query.format(dept_id=2)
db_cursor.execute(r_query)
print(db_cursor.fetchall())






# DDL

sql_employee = """
CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL,
    location  VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)  ENGINE=INNODB;
"""

db_cursor.execute(sql_employee)
db_cursor.connection.commit()

