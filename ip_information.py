from colorama import Fore 
import time
import sys
import ipapi
import menuConfigure
from socket import getfqdn , gethostbyname


def __start__():
        try:
                menuConfigure.banner()

                print("your ip is "+ Fore.RED + gethostbyname(getfqdn())) #Show ip Adress
                print(Fore.GREEN + "ENTER IP ADDRESS :") #Enter ip Adress
                ipAdder = input(Fore.YELLOW+">>>")

                ipSource = ipapi.location(ip=ipAdder, key=None)

                #---Result of ip Address-----------

                print(Fore.CYAN+"your ip is "+ ipSource["ip"])
                time.sleep(0.5)
                print(Fore.LIGHTGREEN_EX+"your city is "+ ipSource["city"])
                time.sleep(0.5)
                print(Fore.CYAN+"your region is "+ ipSource["region"])
                time.sleep(0.5)
                print(Fore.CYAN+"your region Code is "+ ipSource["region_code"])
                time.sleep(0.5)
                print(Fore.LIGHTGREEN_EX+"your id country is "+ ipSource["country"])
                time.sleep(0.5)
                print(Fore.LIGHTGREEN_EX+"your id country Code is "+ ipSource["country_code"])
                time.sleep(0.5)
                print(Fore.LIGHTGREEN_EX+"your id country Code iso3 is "+ ipSource["country_code_iso3"])
                time.sleep(0.5)
                print(Fore.CYAN+"your country is "+ ipSource["country_name"])
                time.sleep(0.5)
                print(Fore.LIGHTGREEN_EX+"your calling code is "+ ipSource["country_calling_code"])
                time.sleep(0.5)
                print(Fore.CYAN+"your language is "+ ipSource["languages"])
                time.sleep(0.5)
                print(Fore.LIGHTGREEN_EX+"your org is "+ ipSource["org"])
                
                #---we can Use for more info------------------------------------------------------------------------

                '''           
                field_list = ['ip', 'city', 'region', 'region_code', 'country', 'country_code', 'country_code_iso3', 
                'country_capital', 'country_tld', 'country_name', 'continent_code', 'in_eu', 'postal', 
                'latitude', 'longitude', 'timezone', 'utc_offset', 'country_calling_code', 'currency', 
                'currency_name', 'languages', 'country_area', 'country_population', 'latlong', 
                'asn', 'org']
                '''

                # sub menu for Every Tools Functions-------------------------------------------------

                print("---------------------------------------------")
                print(Fore.RED+"Hope it was usefull\n (1)Test Agin \n (2)back to menu \n (3)exit")
                __inp = int(input(">>>"))
                if __inp == 1 :
                        __start__()
                elif __inp == 2 :
                        menuConfigure.firstMenu()
                elif __inp == 3:
                        sys.exit()       
                else :
                        menuConfigure.firstMenu()
                        
        except:        
               
                print(Fore.RED+"your ip not Trusted\n (1)Test Agin \n (2)back to menu \n (3)exit")
                __inp = int(input(">>>"))
                if __inp == 1 :
                        __start__()
                elif __inp == 2 :
                        menuConfigure.firstMenu()
                elif __inp == 3:
                        sys.exit()
                else :
                        menuConfigure.firstMenu()                        
