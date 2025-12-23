import numpy as np

def twoing_deger_hesapla(sol_toplam, sag_toplam):
    #Formül: (PL * PR / 4) * (sum(|L_i/L - R_i/R|))^2
    so = sum(sol_toplam)
    sa = sum(sag_toplam)

    if so == 0 or sa == 0:
        return 0
    
    total = so + sa
    p_so = so / total
    p_sa = sa / total

    top_dif = 0
    for i in range(len(sol_toplam)):
        top_dif += abs((sol_toplam[i] / so) - (sag_toplam[i] / sa))
        twoing_deger = (p_so * p_sa / 4) * (top_dif ** 2)
    return twoing_deger
    
sag_taraf = [8,2]
sol_taraf = [2,8]

skor = twoing_deger_hesapla(sag_taraf, sol_taraf)

print(f"Hesaplanan twoing degeri: {skor:.4f}")

if skor > 0:
    print("Algoritma bu bölünmenin ayırt edici olduğunu saptadı. Başarılı.")