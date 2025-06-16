import streamlit as st
import pandas as pd

def app():
    st.markdown('<div class="gray-box"><h2>Upload Data Saham</h2></div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Unggah file data saham di bawah sini", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df  # Simpan ke session state agar bisa dipakai di halaman lain

    # Tampilkan preview jika df sudah ada di session_state
    if 'df' in st.session_state:
        df = st.session_state.df
        st.markdown('<div class="gray-box"><h4>Preview Data Saham:</h4></div>', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)

        # Tombol Next
        if st.button("Next"):
            st.session_state.page_index += 1
            st.rerun()
    else:
        st.info("⚠️ Silakan unggah file CSV terlebih dahulu.")
