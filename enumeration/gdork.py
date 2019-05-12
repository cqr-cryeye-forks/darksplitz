#!/usr/bin/env python3
import requests
import re

def gdork(page, dork):
    key = "partner-pub-2698861478625135:3033704849"
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'}
    url = "https://cse.google.com/cse.js?cx={}".format(key)
    r = requests.get(url, headers = header, timeout = 5)
    patern = re.compile('"cse_token": "(.+?)",')
    token = re.findall(patern, r.text)[0]
    url = "https://cse.google.com/cse/element/v1?num=10&hl=en&cx={}&safe=off&cse_tok={}&start={}&q={}&callback=x".format(key, token, page, dork)
    r = requests.get(url, headers = header, timeout = 5)
    patern = re.compile('"unescapedUrl": "(.+?)",')
    result = re.findall(patern, r.text)
    jumlah = len(result)
    for x in result:
        print('[+] {}'.format(x))
    return jumlah

def googledork(dork):
    if dork == '':
        print('[?] exe : gdork <dork>')
        return False
    print('[!] Dork : {}'.format(dork))
    gdork(1, dork)
    no = 0
    while True:
        try:
            no = no + 1
            page = str(no) + '1'
            hasil = gdork(page, dork)
            if hasil == 0: break
        except KeyboardInterrupt: break