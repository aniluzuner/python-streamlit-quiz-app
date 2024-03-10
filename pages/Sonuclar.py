import streamlit as st
import Fonksiyonlar as ft

st.header("Sınav Sonuçları")

tab1, tab2 = st.tabs(["Sınav Sonuçları", "Sınav Sil"])

with tab1:
    veriler = ft.Sonuclar()
    
    if len(veriler) > 0:
        tablo = ft.TabloGoster(veriler, "Id", "Sınav Ad", "Doğru Sayısı", "Yanlış Sayısı", "Tarih")
        st.table(tablo)
    else:
        st.header("Kayıtlı Sınav Yok!")

with tab2:
    with st.form("sinavsil", clear_on_submit = True):
        sinavlar = ft.VeriGetir("Sınavlar")
        liste = []
        for sinav in sinavlar:
          liste.append(sinav[1])
        sinavsec = st.selectbox("Sınav Seç", liste)
        sil = st.form_submit_button("Sınav Sil")
        if sil:
          ft.VeriSil("Sınavlar", "Ad", sinavsec)
          st.success("Sınav Silindi")