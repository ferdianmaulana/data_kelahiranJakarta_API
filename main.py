# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 20:05:12 2021

@author: ferdia067662
"""

import pandas as pd
from fastapi import FastAPI
import json

app = FastAPI()

df2019 = pd.read_csv('https://raw.githubusercontent.com/ferdianmaulana/data_kelahiranJakarta_API/master/data_kelahiran_jakarta2019.csv')
df2018 = pd.read_csv('https://raw.githubusercontent.com/ferdianmaulana/data_kelahiranJakarta_API/master/data_kelahiran_jakarta2018.csv')
df2017 = pd.read_csv('https://raw.githubusercontent.com/ferdianmaulana/data_kelahiranJakarta_API/master/data_kelahiran_jakarta2017.csv')
df = pd.DataFrame(df2019).append(df2018).append(df2017)

@app.get("/")
#menampilkan semua data
def read_data(): 
    df_json = df.to_json(orient="records")
    parsed = json.loads(df_json)
    data = json.dumps(parsed, indent=4)
    return data

@app.get("/trendPerTahun")
#menampilkan trend kelahiran penduduk Jakarta setiap tahunnya
def trend_pertahun(): 
    trend = pd.DataFrame(df.groupby('tahun')[['jumlah']].sum()).reset_index() 
    df_json = trend.to_json(orient="records")
    parsed = json.loads(df_json)
    data = json.dumps(parsed, indent=4)    
    return data

@app.get("/perbandinganKota")
#menampilkan perbandingan jumlah kelahiran di setiap kota
def perbandingan_kota():  
    kota = pd.DataFrame(df.groupby('nama_kota')[['jumlah']].sum()).reset_index() 
    df_json = kota.to_json(orient="records")
    parsed = json.loads(df_json)
    data = json.dumps(parsed, indent=4)    
    return data

@app.get("/perbandinganGender")
#menampilkan perbandingan jumlah kelahiran untuk setiap gender
def perbandingan_gender():
    gender = pd.DataFrame(df.groupby('jenis_kelamin')[['jumlah']].sum()).reset_index() 
    df_json = gender.to_json(orient="records")
    parsed = json.loads(df_json)
    data = json.dumps(parsed, indent=4)    
    return data

@app.get("/perbandinganTempatLahir")
#menampilkan perbandingan jumlah kelahiran untuk setiap tempat lahir
def perbandingan_tempatLahir():
    tempat = pd.DataFrame(df.groupby('wilayah')[['jumlah']].sum()).reset_index() 
    df_json = tempat.to_json(orient="records")
    parsed = json.loads(df_json)
    data = json.dumps(parsed, indent=4)    
    return data

