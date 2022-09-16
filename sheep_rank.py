import requests
from config import headers,count,rank_url

if __name__ == '__main__':
    for i in range(count):
        try:
            print(requests.get(rank_url, headers=headers, timeout=10).text)
        except:
            pass