import socket , sys , time
from colorama import Fore
import menuConfigure , ip_information




def __start__():
    menuConfigure.banner()
    try:
        #Enter site Address------------------------------------------------------
        print (Fore.GREEN+"[*] ENTER your Target site \n --> EXAMPLE: site.com")
        site = input (Fore.YELLOW+">>>")
        subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev' ]



        #loop in site subdomains---------------------------------------------------

        for sub in subdom :    

                try:
                        time.sleep(0.2)
                        hosts = str(sub) + "."  + str(site)
                        bypass = socket.gethostbyname(str(hosts)) 
                        print (f"your bypass is : {bypass} | your address is {hosts} ")
                except:
                        pass

        # sub menu for Every Tools Functions-------------------------------------------------

        print("---------------------------------------------")
        print(Fore.RED+"Hope it was usefull\n (1)Test Agin \n (2)ip Informaition \n(3)back to menu \n (4)exit")
        __inp = int(input(">>>"))
        if __inp == 1 :
                __start__()
        elif __inp == 2:
                ip_information.__start__()
        elif __inp == 3 :
                menuConfigure.firstMenu()
        elif __inp == 4:
                sys.exit()
        else :
                menuConfigure.firstMenu()
                           
    except:        
        print(Fore.RED+"--> EXAMPLE: site.com\n (1)Test Agin \n (2)back to menu \n (3)exit")
        __inp = int(input(">>>"))
        if __inp == 1 :
                __start__()
        elif __inp == 2 :
                menuConfigure.firstMenu()
        elif __inp == 3:
                sys.exit()
        else :
                menuConfigure.firstMenu()         

