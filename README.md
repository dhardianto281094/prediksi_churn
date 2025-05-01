# prediksi_churn
streamlit_prediksi_churn

# Telco Customer Churn Prediction App

## 🎯 **Problem Statement**

Dalam industri telekomunikasi, mempertahankan pelanggan yang sudah ada lebih efisien dibandingkan dengan menarik pelanggan baru. Namun, churn (pelanggan berhenti berlangganan) adalah masalah utama yang dihadapi oleh banyak perusahaan telekomunikasi. Identifikasi pelanggan yang berpotensi churn sangat penting untuk mengambil langkah-langkah preventif, seperti menawarkan promosi, dukungan khusus, atau program loyalitas.

**Masalah yang ingin diselesaikan**:
- Bagaimana cara memprediksi pelanggan yang kemungkinan besar akan churn?
- Bagaimana kita dapat menggunakan data historis untuk merancang strategi retensi yang lebih baik?

Aplikasi ini bertujuan untuk memberikan prediksi churn pelanggan Telco menggunakan model machine learning yang dilatih dengan dataset historis pelanggan. Dengan aplikasi ini, tim marketing dan tim retention dapat mengambil tindakan lebih cepat dan tepat dalam mempertahankan pelanggan.

---

## 🔍 **Penjelasan Aplikasi**

Aplikasi ini memungkinkan pengguna untuk memprediksi apakah seorang pelanggan akan churn berdasarkan beberapa fitur terkait pelanggan. Pengguna cukup mengisi beberapa informasi dasar mengenai pelanggan, dan model machine learning yang sudah dilatih akan memberikan prediksi serta probabilitas apakah pelanggan tersebut berisiko untuk churn atau tidak.

### **Fitur Aplikasi**:

| **Fitur**       | **Deskripsi**                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Overview**    | Visualisasi data dan statistik dasar mengenai dataset pelanggan. Distribusi churn, jenis kontrak, metode pembayaran, dan lebih banyak lagi.        |
| **Prediction**  | Pengguna dapat mengisi data pelanggan seperti jenis kelamin, umur, status pernikahan, lama berlangganan, tagihan bulanan, dan informasi lainnya.  |
| **Documentation** | Dokumentasi lengkap mengenai proyek ini, termasuk metodologi yang digunakan, evaluasi model, dan cara menggunakannya. Termasuk informasi terkait dataset, model machine learning yang digunakan, dan cara untuk menjalankan aplikasi ini di server atau platform cloud. |

---

### **Model yang Digunakan**:

- **XGBoost**: Model ini digunakan untuk memprediksi churn berdasarkan data historis. XGBoost adalah model berbasis pohon keputusan yang terkenal efektif dalam menangani masalah klasifikasi dengan data yang besar dan tidak terstruktur.
  
- **Random Forest**: Model alternatif yang juga digunakan dalam aplikasi ini untuk memberikan prediksi yang lebih robust. Random Forest adalah model ensemble yang menggabungkan banyak pohon keputusan untuk menghasilkan prediksi yang lebih baik.

---

## 📊 **Dataset**

Aplikasi ini menggunakan dataset **Telco Customer Churn** yang mencakup informasi tentang pelanggan dan status langganannya. Dataset ini berisi beberapa fitur penting, antara lain:

| **Fitur**         | **Deskripsi**                                                                                       |
|-------------------|-----------------------------------------------------------------------------------------------------|
| **Gender**        | Jenis kelamin pelanggan (Male/Female)                                                               |
| **Tenure**        | Lama pelanggan berlangganan (dalam bulan)                                                           |
| **InternetType**  | Jenis layanan internet yang digunakan (Fiber optic, DSL, dll)                                       |
| **MonthlyCharge** | Tagihan bulanan pelanggan                                                                            |
| **TotalCharge**   | Total tagihan yang sudah dibayar pelanggan                                                          |
| **ContractType**  | Jenis kontrak pelanggan (Month-to-month, One year, Two year)                                       |

---

## 🧑‍💻 **Cara Menggunakan Aplikasi**

1. **Navigasi ke Halaman Overview**:
   - Di halaman ini, kamu bisa melihat distribusi data dan analisis statistik dasar mengenai pelanggan. Ini akan membantu kamu memahami lebih baik karakteristik pelanggan yang berpotensi churn.
   - Gambar visualisasi dari distribusi data dapat ditampilkan di halaman ini.

2. **Navigasi ke Halaman Prediction**:
   - Masukkan data pelanggan yang ingin diprediksi, seperti jenis kelamin, umur, dan tagihan bulanan.
   - Aplikasi ini akan memberikan prediksi apakah pelanggan tersebut berisiko churn, beserta dengan probabilitasnya.
   - **Gambar Form Input**: Menunjukkan tampilan input form untuk data pelanggan.

3. **Navigasi ke Halaman Documentation**:
   - Halaman ini berisi dokumentasi lengkap mengenai proyek, termasuk penjelasan tentang data, model yang digunakan, serta cara menjalankan aplikasi ini di server.
   - **Gambar Diagram Alur**: Diagram yang menggambarkan alur kerja aplikasi dari input hingga prediksi.

---

## 🛠 **Installation**

Untuk menjalankan aplikasi ini secara lokal, pastikan kamu telah menginstal Python dan semua dependensi yang diperlukan. Berikut adalah langkah-langkah instalasinya:

### 1. Clone repository ini:
```bash
git clone https://github.com/username/streamlit-churn-prediction.git
cd streamlit-churn-prediction

