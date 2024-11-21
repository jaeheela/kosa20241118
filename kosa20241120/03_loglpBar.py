# pip install matplotlib


import re
import matplotlib.pyplot as plt


def extract_client_ips(log_file):
    client_ips = {}


    with open(log_file, 'r') as file:
        for line in file:
            ip_match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
            if ip_match:
                ip = ip_match.group()
                client_ips[ip] = client_ips.get(ip, 0) + 1


    return client_ips


def plot_top_ips(ip_dict, num_top_ips):
    sorted_ips = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)[:num_top_ips]
    ips = [ip[0] for ip in sorted_ips]
    counts = [ip[1] for ip in sorted_ips]


    plt.bar(range(len(ips)), counts)
    plt.xticks(range(len(ips)), ips, rotation=45)
    plt.xlabel('Client IP')
    plt.ylabel('Access Count')
    plt.title(f'Top {num_top_ips} Client IPs by Access Count')
    plt.show()


# 아파치 웹 로그 파일 경로를 지정합니다.
log_file_path = './data/access.log'


# 클라이언트 IP 추출 및 접속 회수 확인
client_ips = extract_client_ips(log_file_path)


# 상위 5개 IP 막대 그래프 표시
num_top_ips = 5
plot_top_ips(client_ips, num_top_ips)
