import sys
import os
from colorama import Fore
import time
import cloudFlare ,ip_information , buildWith ,  dnsRecord , whois , plugins , themes



    
#---show Banner-------------------------------------------------------------------------------
def banner():
    os.system("clear")
    print(Fore.YELLOW+"""
    _____       _     _    _____                              _   
    |  __ \     | |   (_)  / ____|                            | |  
    | |__) |__ _| |__  _  | (___  _   _ _ __  _ __   ___  _ __| |_ 
    |  _  // _` | '_ \| |  \___ \| | | | '_ \| '_ \ / _ \| '__| __|
    | | \ \ (_| | |_) | |  ____) | |_| | |_) | |_) | (_) | |  | |_ 
    |_|  \_\__,_|_.__/|_| |_____/ \__,_| .__/| .__/ \___/|_|   \__|
                                        | |   | |                   
                                        |_|   |_|                   
    """)

#---start menu-----------------------------------------------------------------------------------

def mainMenu():
    banner()

    #--show mainMenu
    print(Fore.LIGHTGREEN_EX+"<<=== Welcome My budy :) ===>>")
    time.sleep(0.2)
    print(Fore.RED+"(1) Tools List")
    time.sleep(0.2)
    print(Fore.GREEN+"(2) Developer")
    time.sleep(0.2)
    print(Fore.LIGHTBLUE_EX+"(3) Exit")

    #choose menu between 1-3
    __number = int(input(Fore.YELLOW+" >>> "))
    if  __number == 3 :
        sys.exit()   
    elif __number == 2:
        print(secondMenu())
    elif __number == 1 :
        print(firstMenu())  



#---Tools list Menu-------------------------------------------------------------
def firstMenu():
    banner()
    #--show list menu
    print(Fore.YELLOW+"*** What Do You Want My budy :) ***")
    time.sleep(0.2)
    print(Fore.RED+"(1) Found ip Location")
    time.sleep(0.2)
    print(Fore.LIGHTMAGENTA_EX+"(2) Sites Config")
    time.sleep(0.2)
    print(Fore.WHITE+ "(3) CloudFlare's ip")
    time.sleep(0.2)
    print(Fore.LIGHTBLUE_EX+"(4) dns Details")
    time.sleep(0.2)
    print(Fore.LIGHTYELLOW_EX+"(5) who is")
    time.sleep(0.2)
    print(Fore.YELLOW+"(6) WP Plugins Founder")
    time.sleep(0.2)
    print(Fore.RED+"(7) WP Themes Founder")

    #--show exit menu
    time.sleep(0.2)
    print("--------------------------------")
    time.sleep(0.2)
    print(Fore.LIGHTBLUE_EX+"(9) Back to MainMenu")
    time.sleep(0.2)
    print(Fore.LIGHTYELLOW_EX+"(10) Exit")


    #--choose menu between 1-7
    try :
        __number = int(input(Fore.YELLOW+" >>> "))
        if __number == 9 :
            mainMenu()
        elif __number == 10 :
            sys.exit()
        elif  __number == 1 :
            ip_information.__start__()
        elif __number == 2:
            buildWith.__start__()
        elif __number == 3 :
            cloudFlare.__start__()
        elif __number == 4 :
            dnsRecord.__start__()
        elif __number == 5 :
            whois.__start__()
        elif __number == 6 :
            plugins.__start__()  
        elif __number == 7 :
            themes.__start__()   
       
    except:
        print("Invalid Inputs")        
        

#---number 2 in main menu--------------------------------------------------------
def secondMenu():
    banner()

    #--show Informaiion
    time.sleep(0.2)
    print(Fore.YELLOW+"*** Developer : MehrabHei ***")
    time.sleep(0.2)
    print(Fore.YELLOW+"*** Git Hub   : MehrabHei  ***")
    time.sleep(0.2)
    print(Fore.YELLOW+"*** Instagram : MehrabHei ***")
    time.sleep(0.2)
    print(Fore.YELLOW+"*** YouTube   : MehrabHei ***")
    time.sleep(0.2)
    print(Fore.YELLOW+"*** Site      : MehrabHei ***")
    time.sleep(0.2)

    #--exit menu
    print(Fore.RED+"Your next Move ?\n (1)back to menu \n (2)exit")
    __inp = int(input(">>>"))
    if __inp == 1 :
        mainMenu()
    elif __inp == 2 :
        print("Good Luck :) ")
        time.sleep(0.5)
        sys.exit()
    else :
        mainMenu()                      
