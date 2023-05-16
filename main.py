import pyodbc as odbc
import sys
import pypyodbc as odbc
import pickle
# import sqlite3
# import sql
DRIVER_NAME='SQL SERVER'
SERVER_NAME='LAPTOP-4LGCB7J7'
DATABASE_NAME='learning difficulties'

connection_string=f"""

    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;

"""
conn=odbc.connect(connection_string)
print(conn)

def qs():
    id=input("Enter your id : ")

    name=input("Enter your Name: ")
    
    age=input("Enter your age : ")
    cursorstu=conn.cursor()
    sql = "insert into [dbo].[Student] ([stu_id],[name],[age]) values (?, ?, ?);"
    
    cursorstu.execute(sql,(id, name, age))
    conn.commit()
    cursorstu.close()

    print(" Hello",name,"I will ask you some questions")
    
    list=[]
    answer=""
    result=[]
    result2=[]
    result3=[]
    # QUESTIONS
    cursor=conn.cursor()
    cursor.execute(" select [Questions] from [dbo].[question] ")
    
   
    # **************************************
    for row in cursor:

        print(row)
        user_answer= input("Enter answer: ")
        
        list.append(user_answer)
    conn.commit()
    
# *******************************************************************
    cursorans=conn.cursor()
    for l in list : 
       sqlans = "insert into [dbo].[S_answers] ( [stu_id] , [answers]) values (?,?);"
       cursorans.execute(sqlans,(id, l))
      
    conn.commit()
    



 
# ANswers
    cursor2=conn.cursor()
    cursor2.execute(""" select [Answers] from [dbo].[answers] """)
    
    for ans in cursor2:
        result.append(ans[0])
    # print (result)    
    conn.commit() 
    
    for i in result:
        for l in list:
            if l==i:
                result2.append(i)
    # print (result2)
    count=0
    for r in result2:
        count=count+1
    counter=count*4
    # print(count)  
    
    
    if 0<=counter<58:
        a="sever disability"
        print(a)
        cursorres=conn.cursor()
        sqlres = "insert into [dbo].[test_] ( [stu_id] ,[result] ) values (?,?);"
    
        cursorres.execute(sqlres,(id, a))
        conn.commit()
    elif 58<=counter<116:
        cursorres=conn.cursor()
        a="moderate disability"
        print(a)
        sqlres = "insert into [dbo].[test_] ( [stu_id] ,[result] ) values (?,?);"
        
        cursorres.execute(sqlres,(id, a))
        conn.commit()
    elif 116<=counter<174:
        cursorres=conn.cursor()
        a="mild disability"
        print(a)
        sqlres = "insert into [dbo].[test_] ( [stu_id] ,[result] ) values (?,?);"
    
        cursorres.execute(sqlres,(id, a))
        conn.commit()
    elif 174<=counter<=232:
        cursorres=conn.cursor()
        a="normal"
        print(a)
        sqlres = "insert into [dbo].[test_] ( [stu_id] ,[result] ) values (?,?);"
    
        cursorres.execute(sqlres,(id, a))
        conn.commit()
    

qs()















