
import pandas as pd
df=pd.read_csv("music.csv",delimiter=";")


class sarkilar:
    def __init__(self,sarki_adi,sarkici,tur):
        self.sarki=sarki_adi
        self.sarkici=sarkici
        self. tur=tur
        self.gecmis=[]
        self.my_spo_playlist=[]

class calmalistesi(sarkilar):
    #super!
    def __init__(self,sarki_adi,sarkici,tur):
        super().__init__(sarki_adi,sarkici,tur)
        self.suan=""

        #yes,artik super devreye giriyor!
    def calinsin(self):
        print("caliniyor {}- {}".format(self.sarki,self.sarkici))
        self.suan="{} {}".format(self.sarkici,self.sarki)  #sarkici + sarki alindi
        #print(self.suan) Suan isimli degiskene yazdik
#--------------------------------------------------------------------------

#su ani buraya append etmek gerekiyor baska classda yazamayız yazabilmek icin inheritance ile baska class a eklemek gerekir
    def gecmise_bak(self):
        self.gecmis.append(self.suan)
        return self.gecmis
        #gecmis listesine eklemem gerek


#----------------------------------------------------------------
class muzikUygulamasi(calmalistesi):
    def __init__(self):
        super().__init__("","","")
        self.my_spo_playlist=[]

    def playliste_ekle(self,tpl):
        self.my_spo_playlist.append(tpl)  #tuple olarak vermem gerekiyor
        return (self.my_spo_playlist)
    
    def playlistim_(self):
        for i in self.my_spo_playlist:
            print("{} {} {}".format(i[0],i[1],i[2]))

#-------------------- girdigin muziklere gore muzik onersin

class Oneri:
    def __init__(self, muzikUygulamasi,veri):
        self.muzikUygulamasi = muzikUygulamasi
        self.veri=veri

    def oneri_sis(self):
        tur = []
        for i in self.muzikUygulamasi.my_spo_playlist:
            tur.append(i[2])
        max_tur = max(set(tur), key=tur.count)

        print("Öneri Türü:", max_tur)

        en_cok_tekrar_eden_tur = self.veri[self.veri["tur"] == max_tur]
        #Cumle
        print("Bunları da sevebilirsin")
        print(en_cok_tekrar_eden_tur)

                


#Sarki cal

sarki1=calmalistesi("lovely","billie eilish","pop")  #calma listesi methodlari cagriliyor

#sarki2=sarkilar("yellow","coldplay","rock")  artik calma listesinin

sarki1.calinsin()
sarki1.gecmise_bak()


#-------------------------------------------------------------
# playlist_yap=muzikUygulamasi("thunderstruck","acdc","hard rock")

# playlist_yap.playliste_ekle()
#---------------------------------------------
playlist_yap=muzikUygulamasi()
try:
    n=int(input("""
                    *******************************
                    Kac sarki eklemek istersin?
                    Cikis icin:0
                    
                    """))
except ValueError:
    print("Gecersiz")
for i in range(n):
    sarkiadi=input("sarki adi?--->")
    sarkici_=input("sarkici?----> ")
    tur_=input("tur?--->")
    t1=(sarkiadi,sarkici_,tur_)
    playlist_yap.playliste_ekle(t1)
    

print("Mevcut Playlist:")
playlist_yap.playlistim_()

# Öneri yap
oneri = Oneri(playlist_yap, df)
oneri.oneri_sis()


