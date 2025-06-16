import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.markdown('<div class="gray-box"><h2>Grafik Harga Penutupan Saham</h2></div>', unsafe_allow_html=True)

    if 'df' in st.session_state:
        df = st.session_state.df.copy()

        # Ubah kolom 'Tanggal' ke datetime hanya jika belum datetime
        if not pd.api.types.is_datetime64_any_dtype(df['Tanggal']):
            df['Tanggal'] = pd.to_datetime(df['Tanggal'], dayfirst=True, errors='coerce')

        # Buang baris yang gagal konversi datetime (NaT)
        df = df.dropna(subset=['Tanggal'])

        # Urutkan berdasarkan tanggal
        df = df.sort_values('Tanggal')

        if df.empty:
            st.error("Data tidak valid atau semua tanggal gagal diubah ke format datetime.")
            return

        # Plot grafik harga penutupan
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(df['Tanggal'], df['Terakhir'], color='blue', linewidth=2)
        ax.set_title("Harga Penutupan Saham", fontsize=14)
        ax.set_xlabel("Tanggal")
        ax.set_ylabel("Harga Penutupan (Terakhir)")
        ax.grid(True)

        st.pyplot(fig)

        # Next
        if st.button("Next"):
            st.session_state.page_index += 1
            st.rerun()
    else:
        st.warning("⚠️Silakan unggah data saham terlebih dahulu melalui halaman sebelumnya.")
