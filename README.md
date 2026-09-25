# 💳 FinanKu: Sistem Prediksi Risiko Gagal Bayar Kartu Kredit

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://prediksi-risiko-finanku-by-elieser.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

## 📌 Deskripsi Proyek
**FinanKu** adalah aplikasi web berbasis *Machine Learning* yang dirancang untuk membantu institusi keuangan mendeteksi dini potensi gagal bayar (*credit default*) pada nasabah kartu kredit. 

Dengan menganalisis pola riwayat finansial nasabah selama **6 bulan terakhir**, sistem ini memberikan peringatan dini sehingga tim bisnis dapat melakukan tindakan preventif seperti penyesuaian limit kredit atau penjadwalan panggilan penagihan.

## 🚀 Live Demo
Aplikasi ini telah di-deploy dan dapat diakses secara publik melalui Streamlit Community Cloud:
👉 **[Coba Aplikasi FinanKu Sekarang](https://prediksi-risiko-finanku-by-elieser.streamlit.app/)**

## 🧠 Pemodelan Machine Learning
Proyek ini membandingkan berbagai algoritma (Logistic Regression, Gradient Boosting, dan Random Forest) melintasi dua skenario observasi waktu (12 bulan vs 6 bulan). 

**Model Terpilih: Random Forest Classifier (Skenario 6 Bulan)**
*   **Alasan Pemilihan:** Mencetak tingkat akurasi tertinggi secara konsisten pada data validasi (~70%) dan menggunakan parameter waktu yang jauh lebih praktis untuk operasional bisnis di dunia nyata (hanya membutuhkan pengamatan 6 bulan).
*   **Fitur Utama (Feature Importance):** Model telah dioptimalkan untuk berfokus pada 6 metrik finansial terpenting:
    1. `Mean Balance` (Rata-rata Saldo)
    2. `Age` (Umur Nasabah)
    3. `Delta Balance` (Perubahan Saldo)
    4. `Avg. Annual Income/Month` (Rata-rata Pendapatan Bulanan)
    5. `Vintage_CR` (Lama Kepemilikan Kartu)
    6. `Active Months` (Jumlah Bulan Aktif)

## 🛠️ Teknologi yang Digunakan
*   **Bahasa Pemrograman:** Python
*   **Data Manipulasi & Analisis:** Pandas, NumPy
*   **Machine Learning:** Scikit-Learn
*   **Model Serialization:** Joblib
*   **Web Framework / Frontend:** Streamlit
*   **Deployment:** Streamlit Community Cloud

## 💻 Cara Menjalankan Secara Lokal
Jika Anda ingin menjalankan proyek ini di komputer lokal, ikuti langkah-langkah berikut:

1. **Clone repository ini:**
   ```bash
   git clone [https://github.com/username-github-anda/prediksi-risiko-finanku.git](https://github.com/username-github-anda/prediksi-risiko-finanku.git)
   cd prediksi-risiko-finanku
