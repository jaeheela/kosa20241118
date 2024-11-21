# generate_data.py — 임의 데이터 생성 및 CSV 파일로 저장
# 이 파일에서는 100개의 임의 학점 데이터를 생성하고, 이를 grade.csv라는 파일로 저장합니다.

import random
import csv

# 임의의 데이터 생성 함수
def generate_data():
    data = []
    for i in range(1, 101):
        kor_score = random.randint(0, 100)
        math_score = random.randint(0, 100)
        
        # 학점 계산 (간단히 점수대별로 학점 부여)
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
        
        # ID, KOR, MATH, GRADE
        data.append([i, kor_score, math_score, grade])
    
    return data

# CSV로 저장
def save_to_csv(data, filename='grade.csv'):
    header = ['ID', 'KOR', 'MATH', 'GRADE']
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

# 임의 데이터 생성 후 CSV로 저장
data = generate_data()
save_to_csv(data)
print("CSV file 'grade.csv' saved.")
