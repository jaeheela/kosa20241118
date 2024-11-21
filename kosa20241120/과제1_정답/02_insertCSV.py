#   3) 이렇게 만든 CSV를 DB에 입력한다.
#     - DBMS는 sqlite를 쓴다. (파일기반 DB)
#     - 테이블 구조는 임의로 한다. (정규화 고려하지 않아도 된다.)
    
import csv
import sqlite3


conn = sqlite3.connect('./data/grade.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students
             (ID TEXT PRIMARY KEY NOT NULL,
             KOR INT NOT NULL,
             MATH INT NOT NULL,
             GRADE TEXT NOT NULL)''')


with open('./data/grade.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO students (ID, KOR, MATH, GRADE) VALUES (?, ?, ?, ?)",
                  (row['ID'], row['KOR'], row['MATH'], row['GRADE']))


conn.commit()
conn.close()