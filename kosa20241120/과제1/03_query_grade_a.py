# query_grade_a.py — DB에서 A 학점인 데이터만 조회
# 이 파일은 SQLite 데이터베이스에서 GRADE가 A인 학점 데이터를 조회하여 출력합니다.

import sqlite3

# DB 연결
def connect_to_db():
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    return conn, cursor

# A 학점인 학생들 조회
def query_grade_a(cursor):
    cursor.execute('''
    SELECT * FROM grades WHERE GRADE = 'A'
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, KOR: {row[1]}, MATH: {row[2]}, GRADE: {row[3]}")

# 실행
if __name__ == "__main__":
    conn, cursor = connect_to_db()  # DB 연결
    query_grade_a(cursor)  # A 학점인 데이터 출력
    conn.close()  # DB 연결 종료
