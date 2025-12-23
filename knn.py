import math

def oklid_mesafesi(nokta1, nokta2):
    # sqrt((x2-x1)^2 + (y2-y1)^2)
    top = 0
    for i in range(len(nokta1)):
        top += (nokta1[i] - nokta2[i]) ** 2
    return math.sqrt(top)

ozellikler = [
    [195, 95], [200, 105], [190, 90], [205, 110], 
    [160, 50], [162, 52], [158, 48], [165, 54],   
    [172, 72], [170, 70], [175, 75], [168, 68]    
]
etiketler = [
    "Basketbolcu", "Basketbolcu", "Basketbolcu", "Basketbolcu",
    "Jokey", "Jokey", "Jokey", "Jokey",
    "Futbolcu", "Futbolcu", "Futbolcu", "Jokey" 
]

def knn_tahmin(egitim_verisi, egitim_etiketleri, yeni_nokta, k = 3):
    mesafeler = []

    for i in range(len(egitim_verisi)):
        mesafe = oklid_mesafesi(egitim_verisi[i], yeni_nokta)
        mesafeler.append((mesafe, egitim_etiketleri[i]))
    
    mesafeler.sort()
    en_yakinlar = mesafeler[:k]

    oylar = []
    for m in en_yakinlar:
        oylar.append(m[1])
    
    tahmin = max(set(oylar), key=oylar.count)
    return tahmin

yeni_kisi = [160, 85]
sonuc = knn_tahmin(ozellikler, etiketler, yeni_kisi, k=3)
print(f"Yeni kişinin tahmini etiketi: {sonuc}")




    