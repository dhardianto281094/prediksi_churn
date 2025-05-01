import streamlit as st
from PIL import Image
import os

def show_documentation():
    st.title("📚 Documentation")
    
    st.markdown("""
    ## 🧠 Tentang Proyek
    Aplikasi ini dibuat untuk memprediksi kemungkinan pelanggan melakukan **churn** (*berhenti berlangganan*)
    berdasarkan data historis pelanggan pada perusahaan Telco.

    ## 🎯 Tujuan Bisnis
    - Mengidentifikasi pelanggan yang berpotensi churn lebih awal.
    - Membantu tim marketing atau retention mengambil tindakan preventif.
    - Meningkatkan retensi dan loyalitas pelanggan.

    ## 🗂️ Dataset
    - **Sumber**: Internal Data Telco
    - **Target**: `Churn` (1 = Churn, 0 = Tidak Churn)
    - **Beberapa fitur penting**:
        - Gender, Tenure, InternetType, ContractType, MonthlyCharges, TotalCharges

    ## ⚙️ Model & Metodologi
    - Model: XGBoost dan Random Forest
    - Tahapan:
        1. Data Cleaning & Encoding
        2. Feature Selection
        3. Split Data (Train-Test)
        4. Model Training
        5. Evaluasi (Accuracy, Recall, F1-Score)
        6. Deployment (Streamlit)

    ## 🧭 Workflow Aplikasi
    """)

    image_path = "data/ChatGPT Image May 1, 2025, 10_47_34 PM.png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Diagram Alur Aplikasi Prediksi Churn", use_column_width=True)
    else:
        st.warning("❗ Gambar workflow tidak ditemukan. Pastikan file ada di folder `data/`.")

    st.markdown("""
    ---
    _Proyek ini dikembangkan oleh **Dimas Hardianto** sebagai bagian dari program Data Science Bootcamp._
    """)
