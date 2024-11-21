# pip install mariadb
import mariadb


def display_table():
    conn = mariadb.connect(
    host="192.168.56.104",   # 호스트 이름 (예: "localhost")
    user="kosa",  # 사용자 이름
    password="kosa1234",  # 비밀번호
    database="kosa"  # 데이터베이스 이름
    )


    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE GRADE = 'A'")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(f'ID: {row[0]}, KOR: {row[1]}, MATH: {row[2]}, GRADE: {row[3]}')
   
if __name__ == '__main__':
    display_table()