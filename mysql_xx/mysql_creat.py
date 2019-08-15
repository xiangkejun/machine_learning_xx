#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 如果数据库连接存在我们可以使用execute()方法来为数据库创建表，如下所示创建表EMPLOYEE：


import MySQLdb

# 打开数据库连接
db= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='xx',
        db ='test',
        )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)


# 关闭数据库连接
db.close()

print("ok")