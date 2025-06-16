import streamlit as st
import pandas as pd

def create_lag_features(df, n_lag):
    df_lagged = df[['Tanggal', 'Terakhir']].copy()
    for i in range(1, n_lag + 1):
        df_lagged[f'lag_{i}'] = df_lagged['Terakhir'].shift(i)
    df_lagged = df_lagged.dropna().reset_index(drop=True)
    return df_lagged

def app():
    st.markdown('<div class="gray-box"><h2>Pilih Lag Terbaik</h2></div>', unsafe_allow_html=True)

    if 'df' in st.session_state:
        df = st.session_state.df.copy()

        # Himbauan pemilihan lag
        st.info(
            "🔍 **Panduan Pemilihan Lag:**\n"
            "- Lag **1–3**: untuk prediksi cepat (harian).\n"
            "- Lag **4–7**: untuk tren mingguan.\n"
            "- Lag **8–15**: untuk tren jangka panjang.\n"
            "- Jika ragu, gunakan **lag = 3 atau 5**."
        )

        # Ambil nilai n_lag sebelumnya jika sudah ada, jika belum default ke 3
        default_lag = st.session_state.get("n_lag", 3)
        n_lag = st.slider("Pilih jumlah lag (1-15):", min_value=1, max_value=15, value=default_lag)
        st.session_state.n_lag = n_lag  # Simpan ke session_state

        # Buat dan simpan df_lagged jika belum ada atau jika n_lag berubah
        if 'df_lagged' not in st.session_state or st.session_state.get('last_lag_used') != n_lag:
            df_lagged = create_lag_features(df, n_lag)
            st.session_state.df_lagged = df_lagged
            st.session_state.last_lag_used = n_lag  # Simpan lag terakhir untuk tracking

        df_lagged = st.session_state.df_lagged

        st.markdown('<div class="gray-box"><h4>Data Saham dengan Lag:</h4></div>', unsafe_allow_html=True)
        st.dataframe(df_lagged.head(20), use_container_width=True)

        # Tombol Next
        if st.button("Next"):
            st.session_state.page_index += 1
            st.rerun()
    else:
        st.warning("⚠️ Silakan unggah data terlebih dahulu.")
