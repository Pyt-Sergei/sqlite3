import sqlite3 as sql
con=sql.Connection('student.sqlite')
cur=con.cursor()



#INSERT_INSERT_INSERT_INSERT_INSERT_INSERT_INSERT_INSERT_INSERT_



cur.execute("INSERT INTO Study_Group(id_direction,study_year,number)\
            VALUES((SELECT id_direction FROM Direction\
            WHERE short_name='ПМ'),4,1) ")                  #2

cur.execute("INSERT INTO Study_Group(id_direction,study_year,number)\
            VALUES((SELECT id_direction FROM Direction\
            WHERE short_name='ПМ'),3,1) ")           #2

cur.execute("INSERT INTO Study_Group(id_direction,study_year,number)\
            VALUES((SELECT id_direction FROM Direction\
            WHERE short_name='ФИ'),4,1) ")                  #2




cur.execute("INSERT INTO Direction(code,full_name,short_name,short_num)\
            VALUES('03.01.04','Математика','МА',3) ")     #1







cur.execute("SELECT* FROM Direction ")
for x in cur:
     print(x)

cur.execute("SELECT '02'||G.study_year||D.short_num||G.number,\
            G.id_study_group FROM Study_Group G JOIN Direction D ON\
            G.id_direction=D.id_direction ")    
for x in cur:
    print(x)



             





