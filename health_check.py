import sys
import time
import yaml
import requests
from collections import defaultdict
from urllib.parse import urlparse

def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def check_health(endpoint):
    method = endpoint.get('method', 'GET')
    url = endpoint['url']
    headers = endpoint.get('headers', {})
    body = endpoint.get('body', None)

    start_time = time.time()
    try:
        response = requests.request(method, url, headers=headers, data=body, timeout=0.5)
        latency = (time.time() - start_time) * 1000
        return response.status_code >= 200 and response.status_code < 300 and latency < 500
    except requests.exceptions.RequestException:
        return False

def main(file_path):
    config = load_config(file_path)
    domain_stats = defaultdict(lambda: {'up': 0, 'total': 0})

    while True:
        for endpoint in config:
            is_up = check_health(endpoint)
            domain = urlparse(endpoint['url']).netloc
            domain_stats[domain]['total'] += 1
            if is_up:
                domain_stats[domain]['up'] += 1

            availability_percentage = 100 * domain_stats[domain]['up'] / domain_stats[domain]['total']
            print(f"{domain} has {availability_percentage:.0f}% availability percentage")

        time.sleep(15)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python health_check.py <config_file_path>")
        sys.exit(1)

    main(sys.argv[1])
