import streamlit as st
import Fonksiyonlar as ft

st.title("Hoşgeldiniz")

st.header(f'Ders Sayısı {len(ft.VeriGetir("Dersler"))}')
st.header(f'Konu Sayısı {len(ft.VeriGetir("Konular"))}')
st.header(f'Soru Sayısı {len(ft.VeriGetir("Sorular"))}')