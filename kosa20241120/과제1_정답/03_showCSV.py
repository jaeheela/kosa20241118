#   4) DB에 저장된 데이터에서 A 학점인 것만 찾어서 출력한다.
#    - select ~ where
   
import sqlite3


def display_table():
    conn = sqlite3.connect('./data/grade.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE GRADE = 'A'")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(f'ID: {row[0]}, KOR: {row[1]}, MATH: {row[2]}, GRADE: {row[3]}')
   
if __name__ == '__main__':
    display_table()