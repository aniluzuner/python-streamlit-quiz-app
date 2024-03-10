import streamlit as st
import Fonksiyonlar as ft

st.header("Konular")

tab1, tab2, tab3 = st.tabs(["Konular", "Konu Ekle", "Konu Sil"])

with tab1:
  veriler = ft.VeriGetir("Konular")
  
  if len(veriler) > 0:
    tablo = ft.TabloGoster(veriler, "Id", "Konu Adı", "Ders Id")
    st.table(tablo)
  else:
    st.header("Kayıtlı Konu Yok!")
    
with tab2:
  with st.form("konuekle", clear_on_submit = True):
    konu_ad = st.text_input("Konu Adı:")
    
    dersler = ft.VeriGetir("Dersler")
    liste = []
    for ders in dersler:
      liste.append(ders[1])
    derssec = st.selectbox("Ders Seç", liste)
    
    konu_ekle = st.form_submit_button("Konu Ekle")
    
    if konu_ekle:
      for ders in dersler:
        if ders[1] == derssec:
          secilenders = ders[0]
          
      ft.VeriEkle("Konular", konu_ad, secilenders)
      st.success("Konu Başarıyla Eklendi!")
      st.balloons()

with tab3:
  with st.form("konusil", clear_on_submit = True):
    konular = ft.VeriGetir("Konular")
    liste = []
    for konu in konular:
      liste.append(konu[1])
    konusec = st.selectbox("Konu Seç", liste)
    sil = st.form_submit_button("Konu Sil")
    if sil:
      ft.VeriSil("Konular", "Ad", konusec)
      st.success("Konu Silindi")