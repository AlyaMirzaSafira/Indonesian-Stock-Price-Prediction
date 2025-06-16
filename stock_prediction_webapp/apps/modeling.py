import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb

def app():
    st.markdown('<div class="gray-box"><h2>Modeling XGBoost - APSO</h2></div>', unsafe_allow_html=True)

    # Tambahkan pedoman singkat pemilihan hyperparameter
    st.info(
        "📌 **Pedoman Singkat Pemilihan Hyperparameter:**\n"
        "- `n_estimators`: **100–200** → jumlah pohon, lebih besar = prediksi lebih stabil\n"
        "- `max_depth`: **3–5** → kedalaman pohon, lebih tinggi = tangkap pola kompleks\n"
        "- `learning_rate`: **0.05–0.3** → kecepatan belajar, lebih kecil = lebih akurat tapi lambat\n"
        "- `subsample`: **0.6–1.0** → proporsi data tiap pohon, cegah overfitting\n"
        "- `colsample_bytree`: **0.6–1.0** → proporsi fitur tiap pohon\n"
        "- `min_split_loss`: **1.0–5.0** → batas minimum pemisahan, lebih tinggi = pohon lebih simpel\n"
        "- `reg_alpha`: **0.0–5.0** → regularisasi L1, cegah overfitting\n"
        "- `reg_lambda`: **0.0–5.0** → regularisasi L2, stabilkan model\n\n"
        "💡 *Jika bingung, gunakan nilai default berikut untuk hasil awal yang seimbang:*\n"
        "- `n_estimators`: **150**\n"
        "- `max_depth`: **4**\n"
        "- `learning_rate`: **0.1**\n"
        "- `subsample`: **0.7**\n"
        "- `colsample_bytree`: **0.7**\n"
        "- `min_split_loss`: **3.0**\n"
        "- `reg_alpha`: **5.0**\n"
        "- `reg_lambda`: **5.0**"
    )

    if 'df_lagged' in st.session_state:
        df_lagged = st.session_state.df_lagged.copy()

        # Pemisahan fitur dan target
        X = df_lagged.drop(columns=['Tanggal', 'Terakhir'])
        y = df_lagged['Terakhir']

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        st.markdown('<div class="gray-box"><h4>Input Hyperparameter XGBoost</h4></div>', unsafe_allow_html=True)

        # Ambil nilai dari session_state jika ada
        n_estimators = st.number_input("n_estimators", min_value=100, max_value=200,
            value=st.session_state.get("n_estimators", 150), step=10)
        max_depth = st.number_input("max_depth", min_value=3, max_value=5,
            value=st.session_state.get("max_depth", 4), step=1)
        learning_rate = st.number_input("learning_rate", min_value=0.01, max_value=1.0,
            value=st.session_state.get("learning_rate", 0.1), step=0.01, format="%.3f")
        subsample = st.number_input("subsample", min_value=0.5, max_value=1.0,
            value=st.session_state.get("subsample", 0.7), step=0.1, format="%.1f")
        colsample_bytree = st.number_input("colsample_bytree", min_value=0.5, max_value=1.0,
            value=st.session_state.get("colsample_bytree", 0.7), step=0.1, format="%.1f")
        min_split_loss = st.number_input("min_split_loss", min_value=1.0, max_value=5.0,
            value=st.session_state.get("min_split_loss", 3.0), step=0.1)
        reg_alpha = st.number_input("reg_alpha", min_value=0.0, max_value=10.0,
            value=st.session_state.get("reg_alpha", 5.0), step=0.1)
        reg_lambda = st.number_input("reg_lambda", min_value=0.0, max_value=10.0,
            value=st.session_state.get("reg_lambda", 5.0), step=0.1)

        # Tombol Train
        if st.button("Train Model"):
            # Simpan hyperparameter ke session_state
            st.session_state.n_estimators = n_estimators
            st.session_state.max_depth = max_depth
            st.session_state.learning_rate = learning_rate
            st.session_state.subsample = subsample
            st.session_state.colsample_bytree = colsample_bytree
            st.session_state.min_split_loss = min_split_loss
            st.session_state.reg_alpha = reg_alpha
            st.session_state.reg_lambda = reg_lambda

            # Latih model
            model = xgb.XGBRegressor(
                n_estimators=n_estimators,
                max_depth=max_depth,
                learning_rate=learning_rate,
                subsample=subsample,
                colsample_bytree=colsample_bytree,
                gamma=min_split_loss,
                reg_alpha=reg_alpha,
                reg_lambda=reg_lambda,
                objective='reg:squarederror'
            )
            model.fit(X_train, y_train)

            # Simpan ke session_state
            st.session_state.model = model
            st.session_state.final_model = model
            st.session_state.X_train = X_train
            st.session_state.X_test = X_test
            st.session_state.y_train = y_train
            st.session_state.y_test = y_test
            st.session_state.X = X
            st.session_state.y = y
            st.session_state.df_hist = df_lagged[['Tanggal', 'Terakhir']].copy()

            st.success("✅ Model berhasil dilatih.")

        # Tombol Next jika model sudah ada
        if 'model' in st.session_state:
            if st.button("Next"):
                st.session_state.page_index += 1
                st.rerun()
    else:
        st.warning("⚠️ Silakan unggah data dan pilih lag terlebih dahulu pada halaman sebelumnya.")
