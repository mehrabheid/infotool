
#from multiprocessing import Value
import sys , builtwith
from colorama import Fore
import menuConfigure

def __start__():

        try:
            menuConfigure.banner()
            
            #Enter Site Address----------------------------------------------------
              
            target = input("ENTER your domain \n =>")
            if not 'http://' or not 'https://' in target :
                target = 'http://' + target

                records = builtwith.parse(target)
                for name in records:
                        value = ''
                        for val in records[str(name)]:
                                name = name.replace('-',' ')
                                name = name.title()
                                value += str(val) 
                        print(Fore.BLUE+"\n"+name+': '+value)


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
               
                print(Fore.RED+"your site not Trusted\n (1)Test Agin \n (2)back to menu \n (3)exit")
                __inp = int(input(">>>"))
                if __inp == 1 :
                        __start__()
                elif __inp == 2 :
                        menuConfigure.firstMenu()
                elif __inp == 3:
                        sys.exit()
                else :
                        menuConfigure.firstMenu()

