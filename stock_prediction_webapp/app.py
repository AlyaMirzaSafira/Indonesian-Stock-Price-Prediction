import streamlit as st
from multiapp import MultiApp
from apps import home, upload, grafik, lag_selection, modeling, prediction, evaluation, done

app = MultiApp()

st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            background-color: #e0e0e0;
        }
        .block-container {
            padding-top: 2rem;
        }
        .main > div {
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
        }
        .stButton>button {
            width: 200px;
            height: 45px;
            font-size: 16px;
            font-weight: bold;
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        }
        .gray-box {
            background-color: #4f4f4f;
            padding: 1.5rem;
            border-radius: 10px;
            color: white;
            width: 100%;
            text-align: center;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

app.add_app("📌 Home", home.app)
app.add_app("📁 Upload Data Saham", upload.app)
app.add_app("📈 Grafik Harga Penutupan", grafik.app)
app.add_app(" ⏱ Pilih Lag Terbaik", lag_selection.app)
app.add_app("⚙️ Modeling XGBoost-APSO", modeling.app)
app.add_app("🔮 Prediksi Harga 7 Hari Kedepan", prediction.app)
app.add_app("📊 Evaluasi Model", evaluation.app)
app.add_app("✅ Selesai", done.app)

app.run()
