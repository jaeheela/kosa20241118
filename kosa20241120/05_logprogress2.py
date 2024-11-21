# Q2) 로그 파일에서 클라이언트 IP를 추출해서 가장 많이 접속한 IP 5개를 막대 챠트로 그린다.
# Q3) 로그 파일에서 접속 URL을 추출해서 가장 많이 접속한 URL 5개를 파이 챠트로 그린다.


import os
import re
from collections import Counter
import matplotlib.pyplot as plt

# 파일 경로 설정
file_path = 'data/access.log'
output_dir = 'output'

# 출력 디렉토리 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 파일 경로 존재 여부 확인
if not os.path.exists(file_path):
    print(f"The file {file_path} does not exist. Please check the path.")
else:
    # IP 및 URL을 추출하는 함수
    def parse_log(file_path):
        ip_list = []
        url_list = []
        log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+).*\] "(?:GET|POST|PUT|DELETE|HEAD|OPTIONS) (?P<url>\S+)'
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    match = re.match(log_pattern, line)
                    if match:
                        ip_list.append(match.group('ip'))
                        url_list.append(match.group('url'))
        except Exception as e:
            print(f"An error occurred: {e}")
        
        return ip_list, url_list

    # 데이터 분석 및 시각화
    def visualize_data(ip_list, url_list):
        # 가장 많이 접속한 IP 5개
        top_ips = Counter(ip_list).most_common(5)
        ips, ip_counts = zip(*top_ips)
        
        # 막대 차트 생성
        plt.figure(figsize=(10, 5))
        plt.bar(ips, ip_counts, color='skyblue')
        plt.title('Top 5 Most Frequent IPs')
        plt.xlabel('IP Address')
        plt.ylabel('Number of Accesses')
        bar_chart_path = os.path.join(output_dir, 'top_ips.png')
        plt.savefig(bar_chart_path)  # 차트를 저장
        print(f"Bar chart saved to {bar_chart_path}")
        plt.close()
        
        # 가장 많이 접속한 URL 5개
        top_urls = Counter(url_list).most_common(5)
        urls, url_counts = zip(*top_urls)
        
        # 파이 차트 생성
        plt.figure(figsize=(8, 8))
        plt.pie(url_counts, labels=urls, autopct='%1.1f%%', startangle=140)
        plt.title('Top 5 Most Frequent URLs')
        pie_chart_path = os.path.join(output_dir, 'top_urls.png')
        plt.savefig(pie_chart_path)  # 차트를 저장
        print(f"Pie chart saved to {pie_chart_path}")
        plt.close()

    # 실행
    ip_list, url_list = parse_log(file_path)
    visualize_data(ip_list, url_list)
