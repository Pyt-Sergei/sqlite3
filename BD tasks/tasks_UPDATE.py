import sqlite3 as sql
con=sql.Connection('student.sqlite')
cur=con.cursor()

#UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_



cur.execute("UPDATE Run SET id_language=(SELECT id_language\
            FROM Language WHERE label='python3')\
            WHERE id_language=(SELECT id_language FROM Language\
            WHERE label='python') ")                                #1
con.commit()






cur.execute("INSERT INTO Study_Group(id_direction,study_year,number)\
            VALUES((SELECT id_direction FROM Direction\
            WHERE short_name='ФИ'),4,1) ") #3

cur.execute("UPDATE Student SET id_study_group=(SELECT \
            G.id_study_group FROM Study_Group G\
            JOIN Direction D ON G.id_direction=D.id_direction\
            WHERE G.study_year=4 and G.number=1 and D.short_num=7)\
        WHERE SUBSTR(first_name, 1, 1)='А' ")
con.commit()

cur.execute("SELECT* FROM Student WHERE id_study_group=\
           (SELECT G.id_study_group FROM Study_Group G\
            JOIN Direction D ON G.id_direction=D.id_direction\
            WHERE G.study_year=4 and G.number=1 and D.short_num=7) ")
for x in cur:
    print(x)
