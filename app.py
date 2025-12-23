import streamlit as st
import math

# --- 1. ALGORİTMALAR (SAF PYTHON) ---
def oklid(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def knn_tahmin(egitim, etiketler, yeni, k):
    mesafeler = sorted([(oklid(egitim[i], yeni), etiketler[i]) for i in range(len(egitim))])
    en_yakinlar = [m[1] for m in mesafeler[:k]]
    return max(set(en_yakinlar), key=en_yakinlar.count), mesafeler[:k]

def gini_hesapla(grup):
    toplam = sum(grup)
    if toplam == 0: return 0
    return 1 - sum([(x/toplam)**2 for x in grup])

def twoing_hesapla(sol, sag):
    so, sa = sum(sol), sum(sag)
    if so == 0 or sa == 0: return 0
    p_so, p_sa = so/(so+sa), sa/(so+sa)
    diff = sum([abs((sol[i]/so) - (sag[i]/sa)) for i in range(len(sol))])
    return (p_so * p_sa / 4) * (diff ** 2)

def kmeans_merkez_bul(noktalar):
    if not noktalar: return [0, 0]
    boy_ort = sum(n[0] for n in noktalar) / len(noktalar)
    kilo_ort = sum(n[1] for n in noktalar) / len(noktalar)
    return [round(boy_ort, 2), round(kilo_ort, 2)]

# --- 2. MODERN ARAYÜZ ---
st.set_page_config(page_title="Veri Madenciliği Portalı", layout="wide")

# HTML/CSS Tasarımı
st.markdown("""
    <style>
    .header { background: linear-gradient(135deg, #ff4b4b, #800000); padding: 30px; border-radius: 15px; text-align: center; color: white; margin-bottom: 30px; }
    .stButton>button { background-color: #ff4b4b; color: white; font-weight: bold; border-radius: 8px; }
    </style>
    <div class="header">
        <h1>🛠️ Veri Madenciliği Algoritma Laboratuvarı</h1>
        <p>Tüm algoritmalar tek bir panelde.</p>
    </div>
    """, unsafe_allow_html=True)

# Yan Menü (Sidebar)
secim = st.sidebar.radio("Çalıştırmak İstediğiniz Algoritma:", 
                         ["1. KNN (Sınıflandırma)", "2. K-Means (Kümeleme)", "3. Gini (Saflık)", "4. Twoing (Ayrıştırma)"])

# --- 3. ALGORİTMALARI ÇALIŞTIRMA ---

if "1. KNN" in secim:
    st.subheader("📍 KNN - K-En Yakın Komşu")
    col1, col2 = st.columns(2)
    with col1:
        boy = st.number_input("Test Boyu (cm)", 140, 220, 170)
        kilo = st.number_input("Test Kilosu (kg)", 40, 130, 70)
    with col2:
        k = st.slider("Komşu Sayısı (K)", 1, 7, 3)
    
    if st.button("Sınıflandır"):
        # Veri setini sağlamlaştırdık
        veriler = [[195, 95], [160, 52], [172, 72], [190, 92], [165, 55], [170, 71], [185, 88], [162, 53]]
        etiketler = ["Basketbolcu", "Jokey", "Futbolcu", "Basketbolcu", "Jokey", "Futbolcu", "Basketbolcu", "Jokey"]
        sonuc, yakinlar = knn_tahmin(veriler, etiketler, [boy, kilo], k)
        st.success(f"Tahmin: **{sonuc}**")
        st.write("En Yakın Komşuların Detayları:")
        st.table([{"Sınıf": m[1], "Mesafe": round(m[0], 2)} for m in yakinlar])

elif "2. K-Means" in secim:
    st.subheader("📊 K-Means - Merkez Hesaplama")
    st.write("Bir kümedeki noktaları girin, size o kümenin yeni merkezini hesaplayalım.")
    nokta_girisi = st.text_area("Noktaları girin (Format: Boy, Kilo - her satıra bir nokta)", "180, 80\n185, 85\n190, 90")
    if st.button("Yeni Merkezi Hesapla"):
        liste = [[float(v) for v in satir.split(",")] for satir in nokta_girisi.split("\n") if "," in satir]
        merkez = kmeans_merkez_bul(liste)
        st.info(f"Hesaplanan Küme Merkezi (Ortalama): **{merkez}**")

elif "3. Gini" in secim:
    st.subheader("⚖️ Gini Impurity")
    girdi = st.text_input("Sınıf dağılımı (Örn: 5, 5 veya 10, 0)", "5, 5")
    if st.button("Gini Skorunu Hesapla"):
        liste = [int(x.strip()) for x in girdi.split(",")]
        st.metric("Gini Sonucu", f"{gini_hesapla(liste):.4f}")

elif "4. Twoing" in secim:
    st.subheader("✂️ Twoing Kriteri")
    c1, c2 = st.columns(2)
    with c1: l_input = st.text_input("Sol Grup Dağılımı", "10, 2")
    with c2: r_input = st.text_input("Sağ Grup Dağılımı", "2, 10")
    if st.button("Twoing Analizi"):
        l = [int(x) for x in l_input.split(",")]
        r = [int(x) for x in r_input.split(",")]
        st.warning(f"Bölünme Kalitesi (Twoing): **{twoing_hesapla(l, r):.4f}**")