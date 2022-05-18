import requests
import sys
from colorama import Fore
import menuConfigure

def __start__():
    try:
        site = input("Enter Domain\n=>")
        dnsLookUp = requests.get('https://api.hackertarget.com/dnslookup/?q='+ site).text
        print(dnsLookUp)
    except:    
        print("Invalid Domain")
        sys.exit()
