import streamlit as st
import Fonksiyonlar as ft

st.title("Sınav")

if 'first_run' not in st.session_state:
    st.session_state.sorular = ft.SinavGetir()
    st.session_state.secilenler = ["X)X"] * 10
    st.session_state.first_run = True


for i in range(0, 10):
    with st.container(border=True):
        st.text(f"Soru {i+1}:")
        st.subheader(st.session_state.sorular[i][1])
        st.session_state.secilenler[i] = st.radio(f"Seçim {i+1}", [f"{chr(65 + i)}) {sayi}" for i, sayi in enumerate(st.session_state.sorular[i][2].split("|"))], index=None)


with st.container():
    with st.form("sinavbitir"):
        sinavad = st.text_input("Sınav Adı")
        sinavbitir = st.form_submit_button("Sınavı Bitir")
        
        if sinavbitir:
            ft.SinavKaydet(sinavad, st.session_state.sorular, st.session_state.secilenler)
            st.success("Sınav Kaydedildi")
    

