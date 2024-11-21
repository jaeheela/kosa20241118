# <Q1>
# data 폴더 안에 access.log가 있다
# access.log의 앞 5줄을 출력해라

import os

def read_log_file(file_path, num_lines=5):
 
    try:
        # 파일 경로가 존재하는지 확인
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")
       
        # 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            # 처음 num_lines줄 읽기
            for i, line in enumerate(file):
                if i >= num_lines:
                    break
                print(f"라인 {i+1}: {line.strip()}")
               
    except FileNotFoundError as e:
        print(f"에러: {e}")
    except Exception as e:
        print(f"파일을 읽는 중 에러가 발생했습니다: {e}")


# 실행 코드
if __name__ == "__main__":
    # 파일 경로 설정
    log_file_path = os.path.join("data", "access.log")
   
    # 함수 호출
    read_log_file(log_file_path)