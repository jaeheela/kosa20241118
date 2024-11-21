#   1) 학점 정보 : ID, KOR, MATH, GRADE
#      - ID: 숫자 (임의, 중복X)
#      - KOR : 국어 점수
#     - MATH : 수학점수
#     - GRAE : A~F
#   2) 파이썬 프로그램을 이용해서 위 조건에 맞는 임의의 데이터 100건을 만든다.
#      이때 해당 결과를 grade.csv로 저장한다.
#       ID, KOR, MATH, GRADE
#       1, 100, 100, A
#       ..  
#       100건.
      
import csv


data = []
for i in range(100):
    student_id = i + 1
    kor_score = 70 + (i % 31)
    math_score = 80 + (i % 21)
    average = (kor_score + math_score) / 2
   
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
   
    data.append((student_id, kor_score, math_score, grade))


with open('./data/grade.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'KOR', 'MATH', 'GRADE'])
    writer.writerows(data)
   
print('Done')


