import requests
from pyfiglet import Figlet
from colorama import *
from fake_useragent import UserAgent

# Başlık
f = Figlet(font='slant')
print(Fore.LIGHTMAGENTA_EX + f.renderText('Admin Finder'))

link = input(Fore.LIGHTGREEN_EX+"hedef link girin örnek(ornek.com) :")

dosya = open("links.txt","r")
dosya_r = dosya.readlines()
dosya.close()
fake = UserAgent()
header = {'User-Agent': fake.random}
for  i in dosya_r:
    try:
        r = requests.get(link + "/" + i, headers=header)
        c = r.url
        a = r.status_code
        if a == 200:
            print("-"*30)
            print(Fore.LIGHTRED_EX+"admin panel bulundu >",i)
            print(Fore.LIGHTYELLOW_EX+"link >",c)
            print("-"*30)
        else:
            print(Fore.LIGHTWHITE_EX+"bulunamadı >",i)
            
    except:
        print("sitemden cıkıldı ")
        break
