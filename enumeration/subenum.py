#!/usr/bin/env python3
import requests
import json
import re

def subdomainenum(domain):
    if domain == '':
        print('[?] exe : subenum example.com')
        return False

    subdo = []
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'}
    try:
        print('[+] Get subdomain from hackertarget')
        url = 'https://api.hackertarget.com/hostsearch/?q={}'.format(domain)
        r = requests.get(url, headers = header, timeout = 5)
        for x in r.text.split('\n'):
            subd =  x.split(',')[0]
            if subd not in subdo:
                subdo.append(subd)
    except KeyboardInterrupt: print('\r[-] hackertarget skiped')
    except: pass

    try:
        print('[+] Get subdomain from threatminer')
        url = 'https://www.threatminer.org/getData.php?e=subdomains_container&q={}&t=0&rt=10&p=1'.format(domain)
        r = requests.get(url, headers = header, timeout = 5)
        patern = re.compile('">(.+?)</a></td>')
        listd = re.findall(patern, r.text)
        for x in listd:
            if x not in subdo:
                subdo.append(x)
    except KeyboardInterrupt: print('\r[-] threatminer skiped')
    except: pass

    try:
        print('[+] Get subdomain from virustotal')
        url = 'https://www.virustotal.com/ui/domains/{}/subdomains'.format(domain)
        r = requests.get(url, headers = header, timeout = 5)
        jso = json.loads(r.text)
        data = jso['data']
        for x in data:
            subd = x['id']
            if subd not in subdo:
                subdo.append(subd)
    except KeyboardInterrupt: print('\r[-] virustotal skiped')
    except: pass

    try:
        print('[+] Get subdomain from threatcrowd')
        url = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}'.format(domain)
        r = requests.get(url, headers = header, timeout = 5)
        jso =  json.loads(r.text)
        listd = jso['subdomains']
        for x in listd:
            if x not in subdo:
                subdo.append(x)
    except KeyboardInterrupt: print('\r[-] threatcrowd skiped')
    except: pass

    try:
        print('[+] Get subdomain from findsubdomains')
        url = 'https://findsubdomains.com/subdomains-of/{}'.format(domain)
        r = requests.get(url, headers = header, timeout = 5)
        patern = re.compile('             (.+?)                      </div>')
        listd = re.findall(patern, r.text)
        for x in listd:
            if domain in x:
                sub = x.replace(' ', '')
                if sub not in subdo:
                    subdo.append(sub)
    except KeyboardInterrupt: print('\r[-] findsubdomains skiped')
    except: pass

    print('[+] ----------------------------------')
    for subs in subdo:
        print('[+] {}'.format(subs))
    print('[+] ----------------------------------')
    print('[?] Total : {} subdomain collected'.format(len(subdo)))