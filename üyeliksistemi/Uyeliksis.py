from ast import Return
import json
from re import S
import random as rd

from joblib import PrintTime


class Uyelik():
    def __init__(self):
        self.durum = True
        self.k_adi = ""
        self.sifre = ""
        self.e_mail = ""
        self.veriler = {}
        self.veriler["Kullanicilar"] = []

    
        


    def secim(self):
        sec = int(input("Lütfen seçiminizi Yapınız"))
        
        while sec < 1 or sec > 4 :
            sec = int(input("Yanlış seçim yaptınız tekrar (1-4) arasında seçiminizi Yapınız"))
        

        return sec


    def devam(self):
       
        self.Menugoster()
        
        secim = self.secim()
        
        
        if secim == 1 :
            self.GirisYap()

        if secim == 2:
            self.KayıtOl()

        if secim == 3 :
            self.SifremiUnuttum()

        if secim == 4 :
            self.Cıkıs()

        with open("veriler.json", "w" ) as dosya:
            json.dump(self.veriler,dosya)
        

    def Menugoster(self):
        giris = input("""
1- Giriş Yap
2- Kayıt Ol
3- Sifremi Unuttum
4- Cıkıs      
         
         
Lütfen yapmak istediğiniz işlemi seçiniz  """)

    
    def GirisYap(self):
        
        self.k_adi = input("Kullanici adi : ")
        self.sifre = input("Sifrenizi giriniz: ")
        
        with open("veriler.json","r") as dosya : 
            self.veriler = json.load(dosya)
            for k in self.veriler["Kullanicilar"]:
                if k["k_adi"] == self.k_adi and k["sifre"] == self.sifre :
                    print("SİSTEME GİRİŞ YAPTINIZ ")
                    break
                else :
                    print("Girmiş oldğunuz bilgiler sistemdew kayıtlı değildir , kayıt olmak ister misiniz ? ")

    def KayıtOl(self):
        self.k_adi = input("Lütfen kayıt olmak istediğiniz kullanıcı adınızı giriniz : ")
        self.sifre = input("Lütfen kayıt olmak istediğiniz sifrenizi giriniz : ")
        self.e_mail = input("Lütfen kayıt olmak istediğiniz e-postanızı giriniz : ")
        
        self.veriler["Kullanicilar"].append({"k_adi" : self.k_adi , "sifre" : self.sifre , "mail" : self.e_mail})
         

        with open("veriler.json","a") as dosya :
            json.dump(self.veriler,dosya)
            






    def SifremiUnuttum(self):
        kullaniciadi = input("Şifrenizi unuttuğunuz kulllanıcı adınızı giriniz")
        
        with open("veriler.json","r") as dosya :
            self.veriler = json.load(dosya)
            for k in self.veriler["Kullanicilar"]:
                if k["k_adi"] == kullaniciadi :
                    
                    rssifre = rd.randrange(100000,1000000)
                    
                    with open("KurtarmaSifreleri.txt","w") as dosya :
                        dosya.write(str(rssifre))
                    
                    dogrulama = int(input("Size bir doğrulama kodu gönderdik lütfen Masaüstünüze gelen doğrulama kodunu giriniz"))
                    
                    
                    
                                    
                    if dogrulama == rssifre :
                        degisim = input("Şifrenizi değiştirmek istiyor musunuz? (e/h) : ")
                        if degisim == "e" :
                            sifre  = input("Değişim  yapmak istediğiniz şifrenizi giriniz : ")
                            with open("veriler.json","w") as dosya :
                                
                                for k in self.veriler["Kullanicilar"]:
                                    if k["k_adi"] == kullaniciadi :
                                        k["sifre"]  = sifre
                                        json.dump(self.veriler,dosya)
                        else : 
                            with open("veriler.json","r") as dosya :
                                self.veriler = json.load(dosya)
                                for k in self.veriler["Kullanicilar"]:
                                    if k["k_adi"] == kullaniciadi :
                                        print("Sifreniz : {} ".format( k["sifre"]))
                else : 
                    print("Girmiş oldugunuz kullanıcı adı sistememimizde yok")
               
                    


    def Cıkıs(self):
        self.durum=False



uye = Uyelik() 
while uye.durum:
    uye.devam()

