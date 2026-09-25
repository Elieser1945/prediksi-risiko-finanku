import streamlit as st
import pandas as pd
import joblib
import time

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Prediksi Risiko FinanKu", page_icon="💳", layout="centered")

# --- INJEKSI CSS UNTUK BACKGROUND GRADASI CERAH ---
st.markdown("""
<style>
    /* Gradasi Biru Cerah ala Fintech */
    .stApp {
        background: linear-gradient(135deg, #005AA7, #FFFDE4);
        color: #1E1E1E; /* Warna teks utama gelap */
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.85);
        color: #1E1E1E;
    }

    /* Memastikan teks pada elemen-elemen tertentu tetap terbaca */
    .stMarkdown, .stText, h1, h2, h3, h4, h5, h6 {
        color: #1E1E1E !important;
    }
    
    /* Input Box */
    div[data-baseweb="input"] {
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)
# -------------------------------------------------------------------

# 2. Memuat Model
@st.cache_resource
def load_model():
    return joblib.load('model_rf_finanku.pkl')

model = load_model()

# 3. Sidebar
with st.sidebar:
    st.title("🏢 FinanKu")
    st.info("Sistem berbasis *Machine Learning* untuk deteksi dini risiko gagal bayar kartu kredit.")
    st.markdown("---")
    st.caption("© 2026 Developed by **Elieser Pasaribu**")
    st.caption("Data Analyst | Data Scientist | Machine Learning")
    #st.caption("© 2026 Nama Anda | Portofolio Data Science")

# 4. Judul Utama
st.title("Selamat Datang di Website Prediksi Risiko Gagal Bayar Kartu Kredit 👋")
st.markdown("""
Website ini menggunakan model **Random Forest** untuk memprediksi potensi nasabah mengalami gagal bayar.
Model ini menganalisis riwayat finansial nasabah selama 6 bulan terakhir, termasuk rata-rata saldo, perubahan saldo, umur, pendapatan tahunan rata-rata, lamanya kepemilikan kartu, dan aktivitas penggunaan.
""")
st.divider()

# 5. Formulir Data Nasabah
st.subheader("📝 Form Data Nasabah")
col1, col2 = st.columns(2)

with col1:
    mean_balance = st.number_input("Rata-rata Saldo (Rp)", min_value=0.0, step=100000.0, help="Total saldo rata-rata selama 6 bulan.")
    delta_balance = st.number_input("Perubahan Saldo (Rp)", step=100000.0, help="Selisih saldo bulan terakhir dengan bulan pertama.")
    vintage_cr = st.number_input("Lama Kepemilikan Kartu (Bulan)", min_value=0, step=1)

with col2:
    age = st.number_input("Umur (Tahun)", min_value=17, max_value=100, step=1)
    avg_income = st.number_input("Rata-rata Pendapatan/Bulan (Rp)", min_value=0.0, step=500000.0)
    active_months = st.number_input("Bulan Aktif (0-6)", min_value=0, max_value=6, step=1)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Tombol Prediksi
if st.button("🔍 Analisis Risiko Nasabah", type="primary", use_container_width=True):
    with st.spinner('Memproses pola riwayat finansial nasabah...'):
        time.sleep(1.5) 
        
        input_data = pd.DataFrame({
            'Mean Balance': [mean_balance],
            'Age': [age],
            'Delta Balance': [delta_balance],
            'Avg. Annual Income/Month': [avg_income],
            'Vintage_CR': [vintage_cr],
            'Active Months': [active_months]
        })
        
        prediksi = model.predict(input_data)[0]
    
    # 7. Hasil Prediksi (Menggunakan Custom HTML agar warna terkunci dan kontras)
    st.divider()
    if prediksi == 1:
        html_error = """
        <div style="background-color: #F8D7DA; color: #721C24; padding: 15px; border-radius: 8px; border: 1px solid #F5C6CB; margin-bottom: 10px;">
            ⚠️ <strong>RISIKO TINGGI:</strong> Nasabah diprediksi berpotensi Gagal Bayar.
        </div>
        """
        html_warning = """
        <div style="background-color: #FFF3CD; color: #856404; padding: 15px; border-radius: 8px; border: 1px solid #FFEEBA;">
            💡 <strong>Tindakan Disarankan:</strong> Segera lakukan peninjauan limit kredit atau jadwalkan panggilan preventif kepada nasabah.
        </div>
        """
        st.markdown(html_error, unsafe_allow_html=True)
        st.markdown(html_warning, unsafe_allow_html=True)
        
    else:
        st.balloons()
        html_success = """
        <div style="background-color: #D4EDDA; color: #155724; padding: 15px; border-radius: 8px; border: 1px solid #C3E6CB; margin-bottom: 10px;">
            ✅ <strong>AMAN:</strong> Nasabah diprediksi Lancar.
        </div>
        """
        html_info = """
        <div style="background-color: #E2E3E5; color: #383D41; padding: 15px; border-radius: 8px; border: 1px solid #D6D8DB;">
            💡 <strong>Tindakan Disarankan:</strong> Tidak ada indikasi anomali. Lakukan pemantauan rutin seperti biasa.
        </div>
        """
        st.markdown(html_success, unsafe_allow_html=True)
        st.markdown(html_info, unsafe_allow_html=True)