# pip install mariadb
import csv
import mariadb


# MariaDB에 연결
conn = mariadb.connect(
    host="192.168.56.104",   # 호스트 이름 (예: "localhost")
    user="kosa",  # 사용자 이름
    password="kosa1234",  # 비밀번호
    database="kosa"  # 데이터베이스 이름
)


c = conn.cursor()


# 테이블이 존재하지 않으면 생성
c.execute('''CREATE TABLE IF NOT EXISTS students (
             ID INT PRIMARY KEY NOT NULL,
             KOR INT NOT NULL,
             MATH INT NOT NULL,
             GRADE varchar(4))''')


# CSV 파일 읽고 데이터 삽입
with open('./data/grade.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO students (ID, KOR, MATH, GRADE) VALUES (?, ?, ?, ?)",
                  (row['ID'], row['KOR'], row['MATH'], row['GRADE']))


# 변경사항 커밋
conn.commit()


# 연결 종료
conn.close()