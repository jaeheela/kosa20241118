import re
import matplotlib.pyplot as plt


def extract_urls(log_file):
    url_counts = {}


    with open(log_file, 'r') as file:
        for line in file:
            url_match = re.search(r'GET\s+(\S+)', line)
            if url_match:
                url = url_match.group(1)
                url_counts[url] = url_counts.get(url, 0) + 1


    return url_counts


def plot_top_urls(url_dict, num_top_urls):
    sorted_urls = sorted(url_dict.items(), key=lambda x: x[1], reverse=True)[:num_top_urls]
    urls = [url[0] for url in sorted_urls]
    counts = [url[1] for url in sorted_urls]


    plt.pie(counts, labels=urls, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title(f'Top {num_top_urls} URLs Distribution')
    plt.show()


# 아파치 웹 로그 파일 경로를 지정합니다.
log_file_path = './data/access.log'


# URL 추출 및 분포 확인
url_counts = extract_urls(log_file_path)


# 상위 5개 URL 파이 차트 표시
num_top_urls = 5
plot_top_urls(url_counts, num_top_urls)
