import streamlit as st

def app():
    st.markdown('<div class="gray-box"><h1>Welcome to Stock Prediction Apps</h1></div>', unsafe_allow_html=True)
    
    #st.image("C:\Users\alyam\stock_prediction_apps\logo.png", use_column_width=True)

    st.markdown(
        """
        <div class="gray-box">
        <h3>Aplikasi Prediksi Saham Menggunakan Metode <b>XGBoost</b> - <b>Adaptive Particle Swarm Optimization (APSO)</b> </h3>
        <p>Ikuti setiap tahapan yang tersedia pada menu navigasi untuk melakukan prediksi harga saham di Indonesia.</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Next
    if st.button("Next"):
        st.session_state.page_index += 1
        st.rerun()