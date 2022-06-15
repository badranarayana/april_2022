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
username = ''
password = 'Sumanit@123'
database = 'demodb'

#import MySQLdb
