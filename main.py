import requests
import argparse
import pprint
import pycurl
from io import BytesIO
import urllib3




def main(url):
    while True:
        print(url)
        urllib3.disable_warnings()
        response = requests.get(url, verify=False)
        print(response.status_code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--url', required=True, help='URL to test')
    args = parser.parse_args()
    main(args.url)







