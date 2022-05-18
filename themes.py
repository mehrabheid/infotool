import sys , requests
import menuConfigure
from colorama import Fore

def __start__():
        
    #menuConfigure.banner()
    try :    
        site = input(Fore.LIGHTCYAN_EX +"ENTER Domain -> EXAMPLE : site.com \n"+Fore.LIGHTYELLOW_EX+">>>")
        site ="http://"+ site +"/wp-content/themes/"
        themes = ['claue','elementor', 'faltsome', 'flatsome-child', 'avada','Pro-Theme', 'ThemeX', 'eCommerce-Gem', 'Ultra-Theme', 'astra', 'Contra', 'Bayan', 'Gunter', 'Newspaper', 'Multio', 'Vogue', 'Jupitor-x', 'Axolot', 'BeTheme', 'avada', 'Veggie', 'Perle', 'Escutcheon', 'Olsen', 'Kenedy', 'Elen', 'Maxwell', 'Rewritten', 'Hemingway', 'Baskerville', 'OnlineMag', 'Zakra', 'Color-mag', 'The', '7', 'Salient', 'Indigo', 'Enfold', 'Overlay', 'Studio-Press', 'Divi']
        
        
        
        for a in themes :
            b = site +a+"/"
            r = requests.get(b)
            if r.status_code == 200:
                print(Fore.GREEN+ a + " in Use")
            elif r.status_code == 403:
                print(Fore.GREEN+ a + " in Use")
            elif r.status_code == 404:
                pass


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
            
            print(Fore.RED+"Your Domain NOT Trusted\n (1)Test Agin \n (2)back to menu \n (3)exit")
            __inp = int(input(">>>"))
            if __inp == 1 :
                    __start__()
            elif __inp == 2 :
                    menuConfigure.firstMenu()
            elif __inp == 3:
                    sys.exit()
            else :
                    menuConfigure.firstMenu()                        
 
