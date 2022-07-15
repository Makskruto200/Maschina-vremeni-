import sqlite3 as sq
from datetime import date
import random 
class BasaData():
    def my(id):
        with sq.connect("main.db") as con:
            cur=con.cursor()
            file_al=  [i for i in cur.execute("SELECT * FROM  file ")]
            p=[]
            for i in file_al:
                if int(i[0])==int(id):
                    p.append(i)
            return p
        
    def random_img():
        with sq.connect("main.db") as con:
            cur=con.cursor()
            file_al=  [i for i in cur.execute("SELECT * FROM  file")]
            t=[i for i in file_al]
            p=[]
            for i in t:
                b=i[1].split(".")
                if b[1] in ["png","jpg","mp4"]:
                    p.append(i)
            s=p[random.randint(0,len(p)-1)]
                  
             
             
            return s
        
    def file(id,file):
        with sq.connect("main.db") as con:
            cur=con.cursor()
            time=date.today()
            file_al=  [i for i in cur.execute("SELECT * FROM  file")]
            t=[i[1] for i in file_al]
            if not file in t:
                cur.execute(f"""INSERT INTO file VALUES ('{id}','{file}','{time}')""")
    def letter(id, message):
        with sq.connect("main.db") as con:
            cur=con.cursor()
            time=date.today()
            cur.execute(f"""INSERT INTO letter VALUES ('{id}','{message}','{time}')""")
    
    
    def login(id):
        with sq.connect("main.db") as con:
            cur=con.cursor()
            users=  [i for i in cur.execute("SELECT * FROM  users")]
            t=[i[0] for i in users]
            if id in t:
                return "Успешная авторизация"
            else:
                cur.execute(f"""INSERT INTO users VALUES ('{id}')""")
                return "Рады вас приветствовать,мой бот поможет оставить или посмотреть послание в будущие)"   
                 
 
