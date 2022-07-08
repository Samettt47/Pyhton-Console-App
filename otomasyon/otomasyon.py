
class Sirket():
    def __init__(self,ad) :
        self.ad = ad 
        self.calisma = True

    def program(self):
        secim = self.menuSecim()

        if secim == 1 :
            self.Calısanekle()
        if secim == 2 :
            self.calısancıkar()
        if secim == 3 :
            ay_yıl_secim = input("Yıllık bazda görmek ister misiniz? ( e/h)")
            if ay_yıl_secim == "e":
                
                self.Maas(hesap ="y")
            else : 
                self.Maas()
        if secim == 4 :
            self.maaslarıver()
        if secim == 5 :
            self.masrafgir()
        if secim == 6 :
            self.gelirgir()
    def menuSecim(self):
        secim = int(input( """**** {} otomasyona hoşgeldiniz ******** 
        1-Calısan ekle 
        2-Calısan Cıkar
        3-Verilecek Maaş göster
        4-Maaşları ver
        5-Maasları gir
        6-Gelir gir

        seçiminizi giriniz
        """.format(self.ad)))
        while secim < 1 or secim > 7 :
            secim = int(input("Yanlış bir değer girdiniz 1-6 arasında  tekrar seçiniz"))

        return secim 

    def Calısanekle(self):
        id = 1
        Ad = input("Çalışan adını giriniz: ")
        Soyad = input("Çalışan soyadı giriniz: ")
        yas = input("Çalışanın yaşını giriniz: ")
        cinsiyet = input("Cinsiyeti giriniz: ")
        maas = input("Çalışan maaşını giriniz: ")

        with open("calisanlar.txt",  "r") as dosya:
            calisanlistesi = dosya.readlines()
        
        if len(calisanlistesi) == 0:
            id = 1
        else : 
            with open("calisanlar.txt" ,"r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1
 
        with open("calisanlar.txt" ,"a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id ,Ad,Soyad,yas,cinsiyet,maas))



    def calısancıkar(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        gcalisanlar = []
        for calisan in calisanlar:
            gcalisanlar.append(" ".join(calisan[:-1].split("-")))

        for calisan in gcalisanlar:
            print(calisan)
        
        secim = int(input("Lütfen çıkarmak istediğiniz çalışanın numarasını cıakrıtnız(1-{}: ".format(len(gcalisanlar))))
        while secim < 1 or secim >len(gcalisanlar):
            secim = int(input("Lütfen (1-{} arasında numara giriniz ".format(gcalisanlar)))

        calisanlar.pop(secim-1)

        sayac = 1
        dcalisanlar = []

        for calisan in calisanlar :
            dcalisanlar.append(str(sayac) + ")" + calisan.split(")")[1])
            sayac += 1
        with open("calisanlar.txt","w") as dosya :
            dosya.writelines(dcalisanlar)

    def Maas(self , hesap = "a"):
        """hesap : a ise aylık , y ise yıllık hesap"""

        with open("calisanlar.txt","r") as dosya :
            calisanlar = dosya.readlines()       
        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        if hesap == "a":            
            print("Bu ay toplam vermeniz gereken maas {} ".format(sum(maaslar)))
        else : 
            print("Bu yıl toplam vermeniz gereken maas {} ".format(sum(maaslar)*12))

    def maaslarıver(self):
        with open("calisanlar.txt","r") as dosya :
            calisanlar = dosya.readlines()
        
        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        toplammaas = sum(maaslar)
        #### bütceden maasi alma ####

        with open("butce.txt") as dosya:
            tbutce = int(dosya.readlines()[0])
            tbutce = tbutce - toplammaas
        
        with open("butce.txt","w") as dosya:
            dosya.write(str(tbutce))

    def masrafgir(self):
        pass
    def gelirgir(self):
        pass 


sirket = Sirket("Samet Bayraktrar")
while sirket.calisma:
    sirket.program()