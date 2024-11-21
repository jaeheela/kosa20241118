# import flask

# 필요한 라이브러리 가져오기
# import sqlite3
import mariadb
from flask import Flask, render_template

# Flask 앱 초기화
app = Flask(__name__)

# 루트 경로("/") 정의
@app.route('/')
def display_table():
    
    # 데이터베이스 연결 및 데이터 조회
    # conn = sqlite3.connect('./data/grade.db')
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
    print(rows)
    
    # 데이터를 웹 페이지로 전달
    return render_template('table.html', rows=rows)

# 애플리케이션 실행
if __name__ == '__main__':
    app.run()
