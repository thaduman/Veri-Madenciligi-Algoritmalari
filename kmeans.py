import math
import random

def oklid_uzakligi(p1, p2):
    toplam = 0
    for i in range(len(p1)):
        toplam += (p1[i] - p2[i]) ** 2
    return math.sqrt(toplam)

def k_means(veriler, k=2, iterasyon=10):
    merkezler = random.sample(veriler, k)
    
    for tur in range(iterasyon):
        kumeler = [[] for _ in range(k)]
        
        for nokta in veriler:
            mesafeler = [oklid_uzakligi(nokta, m) for m in merkezler]
            en_yakin_index = mesafeler.index(min(mesafeler))
            kumeler[en_yakin_index].append(nokta)
            
        yeni_merkezler = []
        for i in range(k):
            if not kumeler[i]:
                yeni_merkezler.append(merkezler[i])
                continue
                

            boyut_sayisi = len(veriler[0])
            yeni_m = []
            for j in range(boyut_sayisi):
                boyut_toplami = sum(nokta[j] for nokta in kumeler[i])
                yeni_m.append(boyut_toplami / len(kumeler[i]))
            yeni_merkezler.append(yeni_m)
            
        merkezler = yeni_merkezler
        print(f"Tur {tur+1}: Merkezler güncellendi.")

    return kumeler, merkezler


veriler = [
    [190, 95], [195, 100], [185, 90], 
    [160, 50], [165, 55], [158, 48],  
    [170, 70], [172, 72]              
]

son_kumeler, son_merkezler = k_means(veriler, k=2)

print("\n--- K-Means Sonuçları ---")
for i, kume in enumerate(son_kumeler):
    print(f"Küme {i+1} (Merkez {son_merkezler[i]}): {kume}")