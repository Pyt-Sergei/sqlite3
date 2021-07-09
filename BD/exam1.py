import sqlite3 as sql
con=sql.Connection('student.sqlite')
cur=con.cursor()
cur.execute("INSERT INTO Student (nik,first_name,middle_name,\
            last_name,id_study_group) \
 SELECT REPLACE(S.nik,'2018','2017'),\
 S.first_name,S.middle_name,\
 S.last_name,(SELECT G1.id_study_group FROM Study_Group G1\
 JOIN Direction D1 ON G1.id_direction=D1.id_direction WHERE\
 D1.short_name='ПМ' and G1.number=1 and G1.study_year=2)\
 FROM Student S JOIN Study_Group G ON\
 S.id_study_group=G.id_study_group JOIN Direction D ON\
 D.id_direction=G.id_direction\
 WHERE G.number=1 and D.short_name='ПМ'")

#cur.execute("SELECT * FROM Student S JOIN Study_Group G ON \
#             S.id_study_group=G.id_study_group WHERE \
#             G.study_year=2")
#for x in cur:
#    print(x)

#con.execute("PRAGMA foreign_keys = ON")

#con.execute("DELETE FROM Direction WHERE short_name='ПМ'")

con.execute("SELECT * FROM Direction")
for x in cur:
    print(x)
 












    
con.close()
