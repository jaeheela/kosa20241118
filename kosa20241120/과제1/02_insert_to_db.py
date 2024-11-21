# insert_to_db.py — CSV 파일을 SQLite DB에 삽입
# 이 파일은 generate_data.py에서 생성된 grade.csv 파일을 읽고, 데이터를 SQLite 데이터베이스에 삽입하는 역할을 합니다.

import sqlite3
import csv

# DB 연결
conn = sqlite3.connect('grades.db')
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    ID INTEGER PRIMARY KEY,
    KOR INTEGER,
    MATH INTEGER,
    GRADE TEXT
)
''')

# CSV 파일에서 데이터 읽고 DB에 삽입
def insert_data_from_csv(filename='grade.csv'):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # 첫 번째 줄은 헤더이므로 건너뜁니다
        for row in reader:
            cursor.execute('''
            INSERT INTO grades (ID, KOR, MATH, GRADE)
            VALUES (?, ?, ?, ?)
            ''', (int(row[0]), int(row[1]), int(row[2]), row[3]))
    conn.commit()

insert_data_from_csv()  # CSV 파일에서 데이터 삽입
print("Data inserted into the database.")
