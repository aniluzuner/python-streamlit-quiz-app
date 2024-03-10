import streamlit as st
import Fonksiyonlar as ft

st.header("Dersler")

tab1, tab2, tab3 = st.tabs(["Dersler", "Ders Ekle", "Ders Sil"])

with tab1:
  veriler = ft.VeriGetir("Dersler")
  
  if len(veriler) > 0:
    tablo = ft.TabloGoster(veriler, "Id", "Ders Adı")
    st.table(tablo)
  else:
    st.header("Kayıtlı Ders Yok!")
    
with tab2:
  with st.form("dersekle", clear_on_submit = True):
    ders_ad = st.text_input("Ders Adı:")
    ders_ekle = st.form_submit_button("Ders Ekle")
    
    if ders_ekle:
      ft.VeriEkle("Dersler", ders_ad)
      st.success("Ders Başarıyla Eklendi!")
      st.balloons()

with tab3:
  with st.form("Ders Sil", clear_on_submit = True):
    dersler = ft.VeriGetir("Dersler")
    liste = []
    for ders in dersler:
      liste.append(ders[1])
    derssec = st.selectbox("Ders Seç", liste)
    sil = st.form_submit_button("Ders Sil")
    if sil:
      ft.VeriSil("Dersler", "Ad", derssec)
      st.success("Ders Silindi")