import requests
from time import sleep

url = input('url: ')
timeout = int(input('timeout: '))

try:
    resp_url = requests.get(url,timeout=timeout).url
except:
    print('Could not connect to the site')
    quit()

def request(url,timeout):
    try:
        resp = requests.get(url,timeout=timeout)
    except:
        quit()

    if resp.url == url or resp_url not in resp.url:
        quit()

    if 'author' in resp.url:
        try:
            print(resp.url.split('/')[4])
        except:
            quit()

count = 1

while True:
    check_url = url + '?author=' + str(count)
    count += 1
    
    request(check_url,timeout)

