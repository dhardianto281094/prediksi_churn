# prediksi_churn/prediction.py

import streamlit as st
import joblib
import pandas as pd
from PIL import Image

# Load model
model = joblib.load('model/churn_model.pkl')

# Fungsi utama halaman prediksi
def show_prediction():
    st.markdown("<h1 style='color:#4CAF50;'>🔍 Prediksi Churn Pelanggan Telco</h1>", unsafe_allow_html=True)
    st.markdown("Masukkan data pelanggan di bawah untuk memprediksi apakah mereka akan *churn* atau tidak.")

    # Logo (dari URL untuk menghindari error file)
    st.image("https://cdn-icons-png.flaticon.com/512/2906/2906270.png", width=100)

    # Buat 2 kolom agar rapi
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Jenis Kelamin", ['Male', 'Female'])
        age = st.slider("Umur", 18, 100, 30)
        senior = st.selectbox("Apakah Senior Citizen?", [0, 1])
        partner = st.selectbox("Memiliki Partner?", ['Yes', 'No'])
        dependents = st.selectbox("Memiliki Tanggungan?", ['Yes', 'No'])
        tenure = st.slider("Lama Berlangganan (bulan)", 0, 72, 12)

    with col2:
        monthly_charges = st.number_input("Tagihan Bulanan", 0.0, 10000.0, 70.0)
        total_charges = st.number_input("Total Tagihan", 0.0, 100000.0, 2000.0)
        contract = st.selectbox("Jenis Kontrak", ['Month-to-month', 'One year', 'Two year'])
        payment_method = st.selectbox("Metode Pembayaran", [
            'Electronic check', 'Mailed check',
            'Bank transfer (automatic)', 'Credit card (automatic)'
        ])

    # Preprocessing input sesuai fitur model
    input_data = pd.DataFrame({
        'Gender_Male': [1 if gender == 'Male' else 0],
        'Seniorcitizen': [senior],
        'Partner_Yes': [1 if partner == 'Yes' else 0],
        'Dependents_Yes': [1 if dependents == 'Yes' else 0],
        'Tenure': [tenure],
        'Monthlycharges': [monthly_charges],
        'Totalcharges': [total_charges],
        'Contract_One year': [1 if contract == 'One year' else 0],
        'Contract_Two year': [1 if contract == 'Two year' else 0],
        'Paymentmethod_Electronic check': [1 if payment_method == 'Electronic check' else 0],
        'Paymentmethod_Mailed check': [1 if payment_method == 'Mailed check' else 0],
        'Paymentmethod_Credit card (automatic)': [1 if payment_method == 'Credit card (automatic)' else 0],
    })

    # Pastikan input sesuai fitur model
    needed_cols = model.feature_names_in_
    for col in needed_cols:
        if col not in input_data.columns:
            input_data[col] = 0
    input_data = input_data[needed_cols]

    st.markdown("---")

    # Tombol Prediksi (dengan style modern)
    predict_button = st.button("🚀 Prediksi Sekarang")

    if predict_button:
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        st.markdown("### Hasil Prediksi:")
        if prediction == 1:
            st.error(f"⚠️ Pelanggan kemungkinan akan *CHURN* dengan probabilitas **{probability:.2%}**")
        else:
            st.success(f"✅ Pelanggan kemungkinan *TIDAK* churn dengan probabilitas **{1 - probability:.2%}**")

