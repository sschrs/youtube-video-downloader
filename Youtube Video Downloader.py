from pytube import YouTube
import time
import os
from pytube import Playlist

def easy(string):
    yt = YouTube(string)
    stream = yt.streams.filter(file_extension="mp4").first()
    print(yt.title+"---> indirme işlemi başladı...")
    stream.download()
    print(yt.title+"---> indirme işlemi tamamlandı...")

def multi():
    liste=[]
    while (True):
        girdi=input("Video URL: ")
        if (girdi=="q"):
            break
        else:
            liste.append(girdi)
    for i in liste:
        try:
            yt=YouTube(i)
            stream = yt.streams.filter(file_extension="mp4").first()
            print(yt.title+"---> indirme işlemi başladı...")
            stream.download()
            print(yt.title+"---> indirme işlemi tamamlandı...")
            print("--------------------------------------------------------------")
        except:
            print("İlgili Url İndirilirken Bir Hata Oluştu...")
    print("Çoklu İndirme İşlemi Tamamlandı...")

def play_list(string):
    pl = Playlist(string)
    pl.populate_video_urls()
    print("İndirme İşlemi Başladı...Bu işlem uzun sürebilir...")
    pl.download_all()
    print("İndirme işlemi tamamlandı...")
    
def ozel(string):
    yt = YouTube(string)
    print("""Bir Çözünürlük Ayarı Seçin:
    1-)1080p
    2-)720p
    3-)480p
    4-)360p
    5-)240p""")
    while (True):
        res=input(">>>")
        if (res=="1"):
            stream = yt.streams.filter(res="1080p").first()
            print(yt.title+"---> indirme işlemi başladı...")
            stream.download()
            print(yt.title+"---> indirme işlemi tamamlandı...")
            break
        elif(res=="2"):
            stream = yt.streams.filter(res="740p").first()
            print(yt.title+"---> indirme işlemi başladı...")
            stream.download()
            print(yt.title+"---> indirme işlemi tamamlandı...")
            break
        elif(res=="3"):
            stream = yt.streams.filter(res="480p").first()
            print(yt.title+"---> indirme işlemi başladı...")
            stream.download()
            print(yt.title+"---> indirme işlemi tamamlandı...")
            break
        elif(res=="4"):
            stream = yt.streams.filter(res="360p").first()
            print(yt.title+"---> indirme işlemi başladı...")
            stream.download()
            print(yt.title+"---> indirme işlemi tamamlandı...")
            break
        elif(res=="5"):
            stream = yt.streams.filter(res="240p").first()
            print(yt.title+"---> indirme işlemi başladı...")
            stream.download()
            print(yt.title+"---> indirme işlemi tamamlandı...")
            break
        else:
            print("Lütfen Geçerli Bir Değer Giriniz")

print("""█████████  █████████  █████████  █████████  █████████  █████████  █████████

███  ███  ███  ███  ███  YOUTUBE VIDEO DOWNLOADER  ███  ███  ███  ███  ███
                           created by #Sschrs

█████████  █████████  █████████  █████████  █████████  █████████  █████████

███  ███  ███  ███  ███ ███  1-)Quick Download  ███  ███  ███  ███  ███  ███
███  ███  ███  ███  ███ ███  2-)Multi Download  ███  ███  ███  ███  ███  ███
███  ███  ███  ███  ███ ███  3-)PList Download  ███  ███  ███  ███  ███  ███
███  ███  ███  ███  ███ ███  4-)Special Down    ███  ███  ███  ███  ███  ███
███  ███  ███  ███  ███ ███  Q-)Exit            ███  ███  ███  ███  ███  ███""")

while (True):
    islem=input("YVD>>>")
    if (islem=="1"):
        girdi=input("YouTube Video URL: ")
        try:
            easy(girdi)
        except:
            print("Bir hata oluştu lütfen doğru adresi girdiğinizden emin olun...")
    elif (islem=="2"):
        multi()
    elif (islem=="3"):
        try:
            girdi2=input("YouTube PlayList URL: ")
            play_list(girdi2)
        except:
            print("Bir hata oluştu lütfen doğru adresi girdiğinizden emin olun...")
        
    elif (islem=="4"):
        girdi3=input("YouTube Video URL: ")
        try:
            ozel(girdi3)
        except:
            print("Aradığınız kriterde video bulunamadı.Doğru adresi girdiğinizden emin olun ve başka bir çözünürlük ayarı seçin...")

    elif(islem=="q"):
        print("Çıkış Yapılıyor...")
        time.sleep(2)
        break
   
    elif(islem=="Q"):
        print("Çıkış Yapılıyor...")
        time.sleep(2)
        break
    else:
        print("Geçerli bir işlem numarası giriniz...")





