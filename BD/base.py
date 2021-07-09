import sqlite3 as sql
import sys
con=sql.Connection('student.sqlite')
cur=con.cursor()
try:
    for x in cur.execute("select sqlite_version()"):
        print(x)
    cur.execute("CREATE TABLE 'Direction' (id_direction INTEGER PRIMARY KEY AUTOINCREMENT,code VARCHAR(32) NOT NULL,full_name VARCHAR(256) NOT NULL,short_name CHAR(2) NOT NULL,short_num INTEGER NOT NULL)")
    cur.execute("INSERT INTO 'Direction' (code,full_name,short_name,short_num) VALUES ('01.03.02','Прикладная математика и информатика','ПМ',2),\
            ('02.03.02','Фундаментальная информатика и информационные технологии','ФИ',7),\
            ('02.03.03','Математическое обеспечение и администрирование информационных систем','МО',4),\
            ('09.03.03','Прикладная информатика','ПИ',6)")
    cur.execute("CREATE TABLE 'Study_Group' (id_study_group INTEGER PRIMARY KEY AUTOINCREMENT,id_direction INTEGER NOT NULL,study_year INTEGER NOT NULL,number INTEGER NOT NULL,\
            FOREIGN KEY (id_direction) REFERENCES Direction(id_direction))")
    cur.execute("INSERT INTO Study_Group (id_direction,study_year,number) VALUES ((SELECT id_direction FROM Direction WHERE code='01.03.02'),1,1)")
    cur.execute("INSERT INTO Study_Group (id_direction,study_year,number) VALUES ((SELECT id_direction FROM Direction WHERE code='01.03.02'),1,2)")
    cur.execute("INSERT INTO Study_Group (id_direction,study_year,number) VALUES ((SELECT id_direction FROM Direction WHERE code='02.03.02'),1,1)")
    cur.execute("INSERT INTO Study_Group (id_direction,study_year,number) VALUES ((SELECT id_direction FROM Direction WHERE code='02.03.03'),1,1)")
    cur.execute("INSERT INTO Study_Group (id_direction,study_year,number) VALUES ((SELECT id_direction FROM Direction WHERE code='02.03.03'),1,2)")
    cur.execute("INSERT INTO Study_Group (id_direction,study_year,number) VALUES ((SELECT id_direction FROM Direction WHERE code='09.03.03'),1,1)")
    gid={"'"+x+"'":y for (x,y) in cur.execute("SELECT '02'|| Study_Group.study_year || Direction.short_num || Study_Group.number,Study_Group.id_study_group FROM Study_Group JOIN Direction ON Study_Group.id_direction=Direction.id_direction")}
    print(gid)
    cur.execute("CREATE TABLE Student (id_student INTEGER PRIMARY KEY AUTOINCREMENT,id_study_group INTEGER NOT NULL,nik VARCHAR(32) NOT NULL,\
            first_name VARCHAR(32) NOT NULL,middle_name VARCHAR(32),last_name VARCHAR(32) NOT NULL, FOREIGN KEY (id_study_group) REFERENCES Study_Group(id_study_group) ON DELETE RESTRICT)")
    fl=open("all.csv","r",encoding='utf-8')
    vals=[]
    for x in fl:
        lst=list(map(lambda y:"'"+y.strip()+"'",x.split(";")))
        lst[0]=str(gid[lst[0]])
        vals.append("("+",".join(lst)+")")
    fl.close()
    cur.execute("INSERT INTO Student (id_study_group,nik,first_name,middle_name,last_name) VALUES "+",".join(vals))
    cur.execute("CREATE TABLE Language (id_language INTEGER PRIMARY KEY AUTOINCREMENT,label VARCHAR(16) NOT NULL,description VARCHAR(1024))");
    cur.execute("CREATE TABLE Problem (id_problem INTEGER PRIMARY KEY AUTOINCREMENT,label CHAR(4) NOT NULL,name VARCHAR(64) NOT NULL,description VARCHAR(1024))");
    fl=open("tasks.cfg","r",encoding='utf-8')
    vals=[]
    sec=None
    for s in fl:
        s=s.strip()
        if len(s)>0 and s[0]=='[' and s[-1]==']':
            gid={a:b for (a,b) in vals}
            if sec=='[language]':
                #print(gid)
                cur.execute("INSERT INTO Language (label,description) values (?,?)",(gid['short_name'],gid['long_name']))
            elif sec=='[problem]':
                #print(gid)
                cur.execute("INSERT INTO Problem (id_problem,label,name) values (?,?,?)",(gid['id'],gid['short_name'],gid['long_name']))
            sec=s
        else:
            tmp=s.split('=')
            if len(tmp)==2:
                vals.append((tmp[0].strip(),tmp[1].strip(' "')))
    fl.close()
    cur.execute("CREATE TABLE Run (id_run INTEGER PRIMARY KEY AUTOINCREMENT,id_student INTEGER NOT NULL,id_problem INTEGER NOT NULL,id_language INTEGER NOT NULL,verdict,year INTEGER NOT NULL\
                ,month INTEGER NOT NULL,day INTEGER NOT NULL,hour INTEGER NOT NULL,min INTEGER NOT NULL,sec NOT NULL,FOREIGN KEY (id_student) REFERENCES Student(id_student),\
                FOREIGN KEY (id_language) REFERENCES Language(id_language),FOREIGN KEY (id_problem) REFERENCES Problem(id_problem))");    
    fl=open("runs.csv","r",encoding='utf-8')
    for s in fl:
        lst=s.split(';')
        print((lst[0],lst[22],lst[27],lst[29],lst[31],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10]))
        cur.execute("INSERT INTO Run VALUES (?,(SELECT id_student FROM Student WHERE nik=?),?,(SELECT id_language FROM Language WHERE label=?),?,?,?,?,?,?,?)",(int(lst[0]),lst[22],lst[27],lst[29],lst[31],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10]))
    con.commit()    
except :
    print(sys.exc_info())
#cur.execute("SELECT * FROM Student where id_study_group=1")
#print(cur.fetchall())
con.close()
