import sqlite3 as sql
con=sql.Connection('student.sqlite')
cur=con.cursor()
cur.execute("SELECT * FROM Direction")
for x in cur:
    print(x)
cur.execute("SELECT * FROM Study_Group")
for x in cur:
    
    print(x)    
#cur.execute("SELECT * FROM Student")
#for x in cur:
#    print(x)
cur.execute("SELECT D.code,D.full_name,D.short_name,\
            '02'||G.study_year||D.short_num||G.number\
            FROM Direction D JOIN Study_Group G ON\
            D.id_direction=G.id_direction")
for x in cur:
    print(x)
cur.execute("SELECT D.code,D.full_name,D.short_name,\
            '02'||G.study_year||D.short_num||G.number,\
            S.first_name,S.last_name,S.nik\
            FROM Direction D JOIN Study_Group G ON\
            D.id_direction=G.id_direction JOIN Student S ON\
            G.id_study_group=S.id_study_group WHERE LENGTH(S.last_name)>10\
            ORDER BY LENGTH(S.last_name),S.first_name,S.last_name")
for x in cur:
    print(x)
cur.execute("SELECT COUNT(id_student),\
            '02'||G.study_year||D.short_num||G.number FROM Student S\
             JOIN Study_Group G ON S.id_study_group=G.id_study_group\
             JOIN Direction D ON D.id_direction=G.id_direction\
             GROUP BY G.id_study_group")
cur.execute("UPDATE Student SET first_name='Артём' WHERE first_name='Артем'")
con.commit()
cur.execute("SELECT * FROM Student WHERE first_name='Артем' or first_name='Артём'")

cur.execute("UPDATE Student SET id_study_group=(\
            SELECT G.id_study_group FROM Study_Group G JOIN Direction D\
            ON D.id_direction=G.id_direction\
            WHERE G.number=1  and D.short_name='ПМ')\
            WHERE first_name='Ольга'") 

cur.execute("SELECT D.code,D.full_name,D.short_name,\
            '02'||G.study_year||D.short_num||G.number,\
            S.first_name,S.last_name,S.nik\
            FROM Direction D JOIN Study_Group G ON\
            D.id_direction=G.id_direction JOIN Student S ON\
            G.id_study_group=S.id_study_group WHERE S.first_name='Ольга'\
            ORDER BY S.first_name,S.last_name")
for x in cur:
    print(x)
con.commit()

cur.execute("UPDATE Problem SET Name='Решил Иван '||Name WHERE id_problem\
            IN (SELECT DISTINCT R.id_problem\
             FROM Student S JOIN Run R ON S.id_student=R.id_student\
             JOIN Problem P ON P.id_problem=R.id_problem\
             WHERE S.first_name='Иван' and R.verdict='OK') ")
cur.execute("SELECT * FROM Problem")
for x in cur:
    print(x)

import datetime
now=datetime.datetime.now
cur.execute("INSERT INTO Run\
(id_problem,id_student,id_language,verdict,year,month,day,hour,min,sec)\
 VALUES\
(78,(SELECT id_student FROM Student WHERE last_name='Кирюшин'),\
    (SELECT id_language FROM Language WHERE label='python3'),'OK',?,\
    ?,?,?,?,?)",(now().year,now().month,now().day,now().hour,now().minute,now().second))

cur.execute("SELECT R.*,P.name,S.first_name,S.last_name\
             FROM Student S JOIN Run R ON S.id_student=R.id_student\
             JOIN Problem P ON P.id_problem=R.id_problem\
             WHERE S.first_name='Иван' and R.verdict='OK' ORDER BY S.last_name,P.id_problem")

for x in cur:
    print(x)




    



con.close()
