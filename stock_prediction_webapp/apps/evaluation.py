import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Fungsi untuk menghitung MAPE
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    non_zero = y_true != 0
    return np.mean(np.abs((y_true[non_zero] - y_pred[non_zero]) / y_true[non_zero])) * 100

def app():
    st.markdown('<div class="gray-box"><h2>📊 Evaluasi Model</h2></div>', unsafe_allow_html=True)

    # Cek ketersediaan data dan model
    required_keys = ['model', 'X_train', 'X_test', 'y_train', 'y_test']
    if not all(key in st.session_state for key in required_keys):
        st.warning("⚠️ Model belum dilatih atau data belum lengkap.")
        return

    # Ambil model dan data
    model = st.session_state.model
    X_train = st.session_state.X_train
    X_test = st.session_state.X_test
    y_train = st.session_state.y_train
    y_test = st.session_state.y_test

    # Prediksi data
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Hitung metrik evaluasi
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

    train_mae = mean_absolute_error(y_train, y_train_pred)
    test_mae = mean_absolute_error(y_test, y_test_pred)

    train_mape = mean_absolute_percentage_error(y_train, y_train_pred)
    test_mape = mean_absolute_percentage_error(y_test, y_test_pred)

    # Buat DataFrame evaluasi
    eval_df = pd.DataFrame({
        "Dataset": ["Train", "Test"],
        "MAPE (%)": [train_mape, test_mape],
        "MAE": [train_mae, test_mae],
        "RMSE": [train_rmse, test_rmse]
    })

    # Tampilkan hasil evaluasi
    st.markdown("### 🔍 Hasil Evaluasi Model")
    st.dataframe(eval_df.style.format({
        "MAPE (%)": "{:.2f}",
        "MAE": "{:.2f}",
        "RMSE": "{:.2f}"
    }), use_container_width=True)

     # Next
    if st.button("Next"):
        st.session_state.page_index += 1
        st.rerun()