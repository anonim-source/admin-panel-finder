import requests

link = input("hedef link girin :")

dosya = open("links.txt","r+")
dosya_r = dosya.readlines()
dosya.close()

for  i in dosya_r:
    try:
        r = requests.get(link + "/" + i)
        c = r.url
        a = r.status_code
        if a == 200:
            print("-"*30)
            print("admin panel bulundu >",i)
            print("link >",c)
            print("-"*30)
        else:
            print("bulunamadı >",i)
            
    except:
        print("sitemden cıkıldı ")
        break
