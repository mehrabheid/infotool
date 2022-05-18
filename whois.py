import requests
import sys
from colorama import Fore
import json

def __start__():
    try:
        site = input("Enter Domain\n=>")
        dnsLookUp = requests.get('https://whois.com/'+ site).text
        a = json.loads(dnsLookUp.content)
        print(a)
    except:    
        print("Invalid Domain")
        sys.exit()
