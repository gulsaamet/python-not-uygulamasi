from msilib.schema import File
def not_hesapla(satir): 
    satir = satir[:-1]
    liste = satir.split(':')

    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar [1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama>85 and ortalama<=100: 
        harf = "Çok İyi"
    elif ortalama>70 and ortalama<=84:
        harf = "İyi"
    elif ortalama>60 and ortalama<=69:
        harf = "Orta"
    elif ortalama> 50 and ortalama<=59:
        harf = "Kötü"
    elif ortalama> 35 and ortalama<=49:
        harf = "Çok Kötü"
    else: 
        harf = "Öğrenci Sınıfta Kalmıştır."

    return ogrenciAdi + ":" + harf + "\n"
    return ogrenciAdi + ":" + harf + "\n"

def notlari_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file: 
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input('Öğrenci Adı: ')
    soyad = input('Öğrenci Soyad: ')
    not1 = input('Not 1: ')
    not2 = input('Not 2: ')
    not3 = input('Not 3: ')

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file: 
        file.write(ad+ ' '+ soyad+ ':'+not1+','+not2+','+not3+'\n')

def notlari_kaydet():
    with open('sinav_notlari.txt',"r",encoding="utf-8") as file: 
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

            with open("sonuclat.txt", "w",encoding="utf-8") as file2: 
                for i in liste:
                    file2.write(i)


while True: 
    islem = input('1- Notları Oku\n2- Not Gir\n3-Notları Kayıt Et\n4-Çıkış\n')

    if islem == '1':
        notlari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kaydet()
    else:
        break

