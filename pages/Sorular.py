import streamlit as st
import Fonksiyonlar as ft

st.header("Sorular")

tab1, tab2, tab3 = st.tabs(["Sorular", "Soru Ekle", "Soru Sil"])

with tab1:
  veriler = ft.SorularTablosu()
  
  if len(veriler) > 0:
    tablo = ft.TabloGoster(veriler, "Id", "Soru", "Doğru Şık", "Ders", "Konu")
    st.table(tablo)
  else:
    st.header("Kayıtlı Soru Yok!")


with tab2:
  with st.form("soruekle", clear_on_submit = True):
    soru = st.text_area("Soru:")
    
    secenekler = [" "] * 5
    secenekler[0] = st.text_input("A Şıkkı:")
    secenekler[1] = st.text_input("B Şıkkı:")
    secenekler[2] = st.text_input("C Şıkkı:")
    secenekler[3] = st.text_input("D Şıkkı:")
    secenekler[4] = st.text_input("E Şıkkı:")
    
    dogrusecenek = st.radio("Doğru Şık", ["A","B","C","D","E"], horizontal=True, index=None)
    
    dersler = ft.VeriGetir("Dersler")
    konular = ft.VeriGetir("Konular")
    
    konuliste = []
    for ders in dersler:
        for konu in konular:
          if konu[2] == ders[0]:
            konuliste.append(ders[1] + ": " + konu[1])
    konusec = st.selectbox("Ders ve Konu Seç", konuliste)

    soru_ekle = st.form_submit_button("Soru Ekle")
    
    if soru_ekle:   
      for konu in konular:
        if konu[1] == konusec.split(": ")[1]:
          secilenkonu = konu[0]
          
      ft.VeriEkle("Sorular", soru, "|".join(secenekler), dogrusecenek, secilenkonu)
      st.success("Soru Başarıyla Eklendi!")
      st.balloons()
      
with tab3:
  with st.form("sorusil", clear_on_submit = True):
    sorular = ft.VeriGetir("Sorular")
    liste = []
    for soru in sorular:
      liste.append(soru[1])
    sorusec = st.selectbox("Soru Seç", liste)
    sil = st.form_submit_button("Soru Sil")
    if sil:
      ft.VeriSil("Sorular", "Soru", sorusec)
      st.success("Soru Silindi")