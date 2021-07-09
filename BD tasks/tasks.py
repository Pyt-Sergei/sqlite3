import sqlite3 as sql
con=sql.Connection('student.sqlite')
cur=con.cursor()





#SELECT_SELECT_SELECT_SELECT_SELECT_SELECT_SELECT_SELECT_SELECT_SELECT_



cur.execute("SELECT S.first_name FROM Student S JOIN\
            Study_Group G ON S.id_study_group=G.id_study_group\
            WHERE G.study_year=1 GROUP BY S.first_name ") #1

cur.execute("SELECT DISTINCT S.first_name FROM Student S JOIN\
           Study_Group G ON S.id_study_group=G.id_study_group\
           ORDER BY S.first_name ")  #1        (2sposob)
#for x in cur:
 #   print(x)


 
cur.execute("SELECT 'students : '||COUNT(S.id_student),D.code,D.full_name\
            FROM Student S JOIN  Study_Group G ON\
            S.id_study_group=G.id_study_group\
            JOIN Direction D ON G.id_direction=D.id_direction\
            WHERE G.study_year=1 GROUP BY D.id_direction ")  #2
#for x in cur:
 #   print(x)


 
cur.execute("SELECT COUNT(first_name),first_name\
            FROM Student GROUP BY first_name\
            ORDER BY COUNT(first_name) DESC ")    #3
#for x in cur:
 #   print(x)



cur.execute("SELECT COUNT(DISTINCT S.id_student),P.name||' '||'№'||P.label FROM Student S JOIN\
              Run R ON S.id_student=R.id_student JOIN Problem P ON\
              R.id_problem=P.id_problem WHERE R.verdict='OK'\
              GROUP BY P.id_problem ORDER BY P.id_problem")   #4 (по какому алгоритму происходит группировка ?? )
for x in cur:
    print(x)





cur.execute("SELECT COUNT( DISTINCT P.id_problem),S.first_name,\
            S.last_name FROM Problem P JOIN Run R\
            ON P.id_problem=R.id_problem JOIN Student S ON\
            S.id_student=R.id_student WHERE R.verdict='OK'\
            GROUP BY S.id_student ORDER BY COUNT( DISTINCT P.id_problem) DESC ")  #5
#for x in cur:
 #   print(x)




cur.execute("SELECT P.name FROM Problem P JOIN Run R\
            ON P.id_problem=R.id_problem WHERE \
            R.verdict='OK' GROUP BY P.id_problem\
            HAVING COUNT(DISTINCT R.id_student)>20  ")       #6 (как действует условие на счётчик ?? )
#for x in cur:
 #   print(x)


cur.execute("SELECT R.id_problem,S.first_name,S.last_name FROM Student S\
           JOIN Run R ON S.id_student=R.id_student WHERE R.verdict='OK' \
            GROUP BY R.id_problem HAVING R.datetime=MIN(R.datetime) ")   #7 (лучший способ)
#for x in cur:
 #   print(x)






#INSERT_INSERT_INSERT_INSERT_INSERT_INSERT_INSERT_INSERT_INSERT_INSERT_INSERT_





#cur.execute("INSERT INTO Study_Group(id_direction,study_year,number)\
 #           VALUES((SELECT id_direction FROM Direction\
  #          WHERE short_name='ПМ'),3,1) ")           #2
#con.commit()
#cur.execute("INSERT INTO Study_Group(id_direction,study_year,number)\
 #            VALUES((SELECT id_direction FROM Direction\
  #           WHERE short_name='ПМ'),4,1) ")                  #2
  
#con.commit()

#cur.execute("INSERT INTO Direction(code,full_name,short_name,short_num)\
 #           VALUES('03.01.04','Математика','МА',3) ")     #1

#con.commit()



#cur.execute("INSERT INTO Student(id_study_group,nik,first_name,middle_name,last_name)\
 #          SELECT 62,REPLACE(nik,'2018','2015'),first_name,\
  #         middle_name,last_name FROM Student WHERE id_study_group=1 ")   #3 РЕШАЛ ПОСЛЕ ЗАДАНИЯ №3 ИЗ UPDATE
#con.commit()



cur.execute("SELECT* FROM Direction ")
for x in cur:
     print(x)
print()
cur.execute("SELECT '02'||G.study_year||D.short_num||G.number,\
            G.id_study_group FROM Study_Group G JOIN Direction D ON\
            G.id_direction=D.id_direction ")    
for x in cur:
    print(x)




#UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_UPDATE_



cur.execute("UPDATE Run SET id_language=(SELECT id_language\
            FROM Language WHERE label='python3')\
            WHERE id_language=(SELECT id_language FROM Language\
            WHERE label='python') ")                                #1
con.commit()


#cur.execute("UPDATE Run SET datetime=\
 #          datetime(datetime, '-1 day') WHERE\
  #         id_student=(SELECT id_student FROM Student\     2
   #        WHERE last_name='Погосян') ")
con.commit()

cur.execute("SELECT* FROM Run WHERE id_student=\
           (SELECT id_student FROM Student WHERE\
           last_name='Погосян') ")
#for x in cur:
 #   print(x)



cur.execute("UPDATE Student SET id_study_group=(SELECT \
            G.id_study_group FROM Study_Group G\
            JOIN Direction D ON G.id_direction=D.id_direction\
            WHERE G.study_year=4 and G.number=1 and D.short_num=7)\
        WHERE SUBSTR(first_name, 1, 1)='А' ")                        #3
con.commit()




cur.execute("SELECT* FROM Student WHERE id_study_group=\
           (SELECT G.id_study_group FROM Study_Group G\
            JOIN Direction D ON G.id_direction=D.id_direction\
            WHERE G.study_year=4 and G.number=1 and D.short_num=2) ")      
#for x in cur:
 #   print(x)




con.close()
