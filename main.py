import requests
import argparse
import pprint
from io import BytesIO
import urllib3
import time

def main(url):
    while True:
        print(url)
        urllib3.disable_warnings()
        response = requests.get(url, verify=False)
        print(response.status_code)
        time.sleep(60)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--url', required=True, help='URL to test, like http(s)://xxx.com')
    args = parser.parse_args()
    main(args.url)







