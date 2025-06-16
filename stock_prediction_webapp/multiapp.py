import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        titles = [app['title'] for app in self.apps]

        # Inisialisasi
        if "manual_nav" not in st.session_state:
            st.session_state.manual_nav = 0
        if "page_index" not in st.session_state:
            st.session_state.page_index = 0

        # Sidebar navigasi manual
        st.session_state.manual_nav = st.sidebar.radio(
            "Navigasi Aplikasi",
            options=list(range(len(titles))),
            format_func=lambda i: titles[i],
            index=st.session_state.page_index,
            key="manual_nav_radio"
        )

        # Sinkronkan navigasi manual ke page_index
        if st.session_state.manual_nav != st.session_state.page_index:
            st.session_state.page_index = st.session_state.manual_nav
            st.rerun()

        # Jalankan halaman aktif
        current_app = self.apps[st.session_state.page_index]
        current_app["function"]()
