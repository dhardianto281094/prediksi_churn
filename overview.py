import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

# Fungsi untuk membersihkan data
def clean_data(df):
    """
    Membersihkan data dan mengatasi error konversi numerik.
    """
    df.columns = df.columns.str.strip()  # Menghapus spasi ekstra pada nama kolom
    if 'Totalcharges' in df.columns:
        df['Totalcharges'] = pd.to_numeric(df['Totalcharges'], errors='coerce')  # Menangani error konversi menjadi NaN
        df = df.dropna(subset=['Totalcharges'])  # Menghapus baris dengan nilai NaN di kolom Totalcharges
    return df

# Fungsi utama untuk menampilkan halaman overview
def show_overview():
    st.title("📊 Telco Churn Overview")
    st.write("Insight pelanggan berdasarkan data yang telah dieksplorasi.")

    # Menu untuk memilih antara latar belakang proyek dan dashboard
    menu = st.radio(
        "Pilih Halaman",
        ('Latar Belakang Proyek', 'Dashboard')
    )

    # Menampilkan latar belakang proyek
    if menu == 'Latar Belakang Proyek':
        st.markdown("""
        ### Latar Belakang Proyek

        Dalam industri telekomunikasi, churn atau pelanggan yang berhenti berlangganan adalah masalah yang serius, karena dapat berdampak pada pendapatan dan pertumbuhan perusahaan. Proyek ini bertujuan untuk menganalisis faktor-faktor yang memengaruhi churn pelanggan pada perusahaan telekomunikasi menggunakan data historis.

        **Tujuan Proyek:**
        - Menganalisis faktor-faktor yang memengaruhi keputusan pelanggan untuk berhenti berlangganan (churn).
        - Mengidentifikasi pola churn berdasarkan atribut demografis, tipe layanan, dan lama berlangganan.
        - Memberikan wawasan yang dapat digunakan oleh tim pemasaran dan pengelola pelanggan untuk mengurangi tingkat churn dan meningkatkan retensi pelanggan.

        **Data yang Digunakan:**
        - Dataset ini mencakup informasi mengenai pelanggan, seperti usia, jenis kelamin, jenis internet yang digunakan, kategori pendapatan, lama berlangganan, dan status churn (apakah pelanggan tersebut masih aktif atau sudah berhenti berlangganan).
        
        **Analisis yang Dilakukan:**
        - Visualisasi distribusi churn, segmentasi berdasarkan pendapatan, dan analisis korelasi antar fitur.
        - Penggunaan berbagai teknik analisis seperti histogram, box plot, heatmap korelasi, dan pie chart untuk menyajikan wawasan yang dapat digunakan oleh perusahaan untuk mengambil keputusan bisnis yang lebih baik.

        Proyek ini bertujuan untuk membantu perusahaan memahami lebih dalam mengenai perilaku pelanggan dan mengidentifikasi strategi yang efektif dalam mengurangi churn.
        """)

    # Menampilkan dashboard analisis data
    elif menu == 'Dashboard':
        try:
            # Load dan bersihkan data
            df = pd.read_csv("telco_customer_churn_final.csv")
            df = clean_data(df)

            st.markdown("### 📋 Overview Dashboard")

            # Layout 2 kolom untuk tampilan yang lebih rapi
            col1, col2 = st.columns(2)

            # 1. Distribusi Churn
            with col1:
                st.subheader("📉 Distribusi Churn")
                churn_counts = df['Churnlabel'].value_counts().reset_index()
                churn_counts.columns = ['Churnlabel', 'Jumlah']
                chart = alt.Chart(churn_counts).mark_bar(color="#ff4b4b").encode(
                    x=alt.X('Churnlabel:N', title='Churn'),
                    y=alt.Y('Jumlah:Q', title='Jumlah Pelanggan'),
                    tooltip=['Churnlabel', 'Jumlah']
                ).properties(width=400, height=300)
                st.altair_chart(chart, use_container_width=True)

            # 2. Distribusi berdasarkan Gender
            with col2:
                st.subheader("👫 Distribusi berdasarkan Gender")
                fig, ax = plt.subplots()
                sns.countplot(data=df, x='Gender', hue='Churnlabel', ax=ax, palette="Set2")
                ax.set_title("Distribusi Churn Berdasarkan Gender")
                st.pyplot(fig)

            # 3. Tipe Internet yang Digunakan Pelanggan
            st.subheader("🌐 Tipe Internet yang Digunakan Pelanggan")
            fig2, ax2 = plt.subplots()
            sns.countplot(data=df, y='Internettype', hue='Churnlabel',
                          order=df['Internettype'].value_counts().index, ax=ax2, palette="coolwarm")
            ax2.set_title("Distribusi Churn Berdasarkan Tipe Internet")
            st.pyplot(fig2)

            # 4. Korelasi Antar Fitur
            st.subheader("🔍 Korelasi Antar Fitur")
            numeric_df = df.select_dtypes(include=['number'])
            corr_matrix = numeric_df.corr()
            fig3, ax3 = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax3, cbar=True)
            ax3.set_title("Heatmap Korelasi Fitur")
            st.pyplot(fig3)

            # 5. Segmentasi Berdasarkan Pendapatan
            st.subheader("💸 Segmentasi Pelanggan Berdasarkan Pendapatan")
            income_churn = df.groupby('IncomeCategory')['Churnlabel'].value_counts(normalize=True).unstack().fillna(0)
            fig5, ax5 = plt.subplots(figsize=(10, 6))
            income_churn.plot(kind='bar', stacked=True, color=["#ff4b4b", "#42b2a5"], ax=ax5)
            ax5.set_title('Segmentasi Churn Berdasarkan Pendapatan')
            ax5.set_xlabel('Kategori Pendapatan')
            ax5.set_ylabel('Proporsi Churn')
            st.pyplot(fig5)

            # 6. Distribusi Churn Berdasarkan Lama Berlangganan
            st.subheader("📅 Distribusi Churn Berdasarkan Lama Berlangganan")
            fig4, ax4 = plt.subplots(figsize=(8, 6))
            sns.boxplot(data=df, x='Churnlabel', y='MonthsOnBook', ax=ax4, palette="coolwarm")
            ax4.set_title("Perbandingan Lama Berlangganan dengan Churn")
            st.pyplot(fig4)

            # 7. Churn Berdasarkan Tipe Internet
            st.subheader("🍰 Churn Berdasarkan Tipe Internet")
            internet_churn = df.groupby('Internettype')['Churnlabel'].value_counts().unstack().fillna(0)
            internet_churn = internet_churn.div(internet_churn.sum(axis=1), axis=0)
            fig6, ax6 = plt.subplots(figsize=(7, 7))
            if 'Churn' in internet_churn.columns:
                internet_churn['Churn'].plot(kind='pie', autopct='%1.1f%%', ax=ax6, colors=["#ff4b4b", "#42b2a5"])
            else:
                internet_churn.iloc[:, 0].plot(kind='pie', autopct='%1.1f%%', ax=ax6, colors=["#ff4b4b", "#42b2a5"])
            ax6.set_ylabel('')
            ax6.set_title('Distribusi Churn Berdasarkan Tipe Internet')
            st.pyplot(fig6)

            # Widget untuk Filter
            st.markdown("### Filter Berdasarkan Kategori Pendapatan")
            income_filter = st.selectbox("Pilih Kategori Pendapatan", df['IncomeCategory'].unique())
            filtered_df = df[df['IncomeCategory'] == income_filter]

            st.write(f"Menampilkan data untuk kategori pendapatan: {income_filter}")
            st.write(filtered_df.head())

        except FileNotFoundError:
            st.error("❌ File CSV tidak ditemukan.")
        except Exception as e:
            st.error(f"Terjadi error: {e}")

# Menjalankan fungsi utama
if __name__ == "__main__":
    show_overview()
