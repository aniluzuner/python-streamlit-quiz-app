import sqlite3
import pandas as pd
import random
from datetime import datetime

def VeriGetir(tablo):
  conn = sqlite3.connect("sorubankasi.sqlite")
  c = conn.cursor()
  sorgu = f"SELECT * FROM {tablo}"
  c.execute(sorgu)
  return c.fetchall()


def VeriEkle(tablo, *veriler):
  conn = sqlite3.connect("sorubankasi.sqlite")
  c = conn.cursor()
  
  veriler = (None,) + veriler
        
  placeholders = ",".join(["?" for _ in veriler])
  
  
  sorgu = f"INSERT INTO {tablo} VALUES ({placeholders})"
  c.execute(sorgu, veriler)
  conn.commit()
 
 
def VeriSil(tablo, sutun, deger):
  conn = sqlite3.connect("sorubankasi.sqlite")
  c = conn.cursor()
  
  sorgu = f"DELETE FROM {tablo} WHERE {sutun} = '{deger}'"
  c.execute(sorgu)
  c.execute(f"UPDATE `sqlite_sequence` SET `seq` = (SELECT MAX(`Id`) FROM {tablo}) WHERE `name` = '{tablo}';")
  conn.commit()
  
  
def TabloGoster(veriler, *sutunlar):
  dataframe = pd.DataFrame(veriler)
  dataframe.columns = sutunlar
  return dataframe


def SorularTablosu():
  conn = sqlite3.connect("sorubankasi.sqlite")
  c = conn.cursor()
  sorgu = f"SELECT S.Id, S.Soru, S.DoğruŞık, D.Ad, K.Ad FROM (Sorular S INNER JOIN Konular K ON S.KonuId = K.Id) INNER JOIN Dersler D ON K.DersId = D.Id"
  c.execute(sorgu)
  return c.fetchall()


def SinavGetir():
  conn = sqlite3.connect("sorubankasi.sqlite")
  c = conn.cursor()
  
  c.execute('SELECT COUNT(*) FROM Sorular')
  toplamsoru = c.fetchone()[0]
  
  
  random_numbers = random.sample(range(1, toplamsoru + 1), 10)
  sorgu = f'SELECT * FROM Sorular WHERE Id IN ({", ".join(map(str, random_numbers))})'
  c.execute(sorgu)
  return c.fetchall()


def SinavKaydet(sinavad, sorular, secilenler):
    conn = sqlite3.connect("sorubankasi.sqlite")
    c = conn.cursor()
    
    dogru = 0
    yanlis = 0
    
    for i, secilen in enumerate(secilenler):
        if secilen == None:
            secilenler[i] = "boş) boş"
        
    for i, soru in enumerate(sorular):
        if soru[3] == secilenler[i].split(") ")[0]:
            dogru += 1
        else:
            yanlis += 1
    
    sorular = ",".join([f"{soru[0]}" for soru in sorular])
    cevaplar = ",".join([secilen.split(") ")[0] for secilen in secilenler])
    sorgu = "INSERT INTO Sınavlar (Ad, Sorular, Cevaplar, Doğru, Yanlış, Tarih) VALUES (?, ?, ?, ?, ?, ?)"
    values = (sinavad, sorular, cevaplar, dogru, yanlis, datetime.now())
    c.execute(sorgu, values)
    conn.commit()


def Sonuclar():
    conn = sqlite3.connect("sorubankasi.sqlite")
    c = conn.cursor()
    
    sorgu = "SELECT Id, Ad, Doğru, Yanlış, Tarih FROM Sınavlar"
    c.execute(sorgu)
    return c.fetchall()
  
  
  