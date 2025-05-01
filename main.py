import streamlit as st
from PIL import Image

# Set up the page configuration
st.set_page_config(
    page_title="Telco Churn Prediction App",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import modul halaman
try:
    from overview import show_overview
    from prediction import show_prediction
    from documentation import show_documentation
except ImportError as e:
    st.error(f"❌ Gagal mengimpor modul halaman: {e}")
    st.stop()

# Sidebar Navigasi
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/893/893257.png", width=80)
    st.title("📂 Menu Navigasi")
    menu = st.radio("Pilih Halaman:", ["📊 Overview", "🔍 Prediction", "📚 Documentation"])
    st.markdown("---")
    st.caption("Dibuat oleh: Dimas Hardianto")

# Header utama
st.markdown(
    """
    <style>
    .main-title {
        font-size:36px !important;
        font-weight: 700;
        color: #4CAF50;
    }
    .main-subtitle {
        font-size:18px !important;
        color: #777;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">📈 Telco Customer Churn Analysis & Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Aplikasi interaktif untuk eksplorasi data pelanggan dan prediksi kemungkinan churn.</div>', unsafe_allow_html=True)
st.markdown("---")

# Routing halaman berdasarkan pilihan
if menu == "📊 Overview":
    show_overview()
elif menu == "🔍 Prediction":
    show_prediction()
elif menu == "📚 Documentation":
    show_documentation()
