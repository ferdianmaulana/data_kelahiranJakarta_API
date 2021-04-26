# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 20:05:12 2021

@author: ferdia067662
"""

import pandas as pd
from fastapi import FastAPI

app = FastAPI()

df2019 = pd.read_csv('data_kelahiran_jakarta2019.csv')
df2018 = pd.read_csv('data_kelahiran_jakarta2018.csv')
df2017 = pd.read_csv('data_kelahiran_jakarta2017.csv')
df = pd.DataFrame(df2019).append(df2018).append(df2017)
df = df.replace('\n','', regex=True)

@app.get("/")
#menampilkan trend kelahiran penduduk Jakarta setiap tahunnya
def trend_per_tahun(): 
    trend = pd.DataFrame(df.groupby('tahun')[['jumlah']].sum()).reset_index() 
    df_str = trend.astype(str)
    df_str.reset_index(drop=True, inplace=True)
    data = df_str.to_dict('records')
    return data

@app.get("/perbandinganKota")
#menampilkan perbandingan jumlah kelahiran di setiap kota
def perbandingan_kota():  
    kota = pd.DataFrame(df.groupby('nama_kota')[['jumlah']].sum()).reset_index() 
    df_str = kota.astype(str)
    df_str.reset_index(drop=True, inplace=True)
    data = df_str.to_dict('records')
    return data

@app.get("/perbandinganGender")
#menampilkan perbandingan jumlah kelahiran untuk setiap gender
def perbandingan_gender():
    gender = pd.DataFrame(df.groupby('jenis_kelamin')[['jumlah']].sum()).reset_index() 
    df_str = gender.astype(str)
    df_str.reset_index(drop=True, inplace=True)
    data = df_str.to_dict('records')
    return data

@app.get("/perbandinganTempatLahir")
#menampilkan perbandingan jumlah kelahiran untuk setiap tempat lahir
def perbandingan_tempat_Lahir():
    tempat = pd.DataFrame(df.groupby('wilayah')[['jumlah']].sum()).reset_index() 
    df_str = tempat.astype(str)
    df_str.reset_index(drop=True, inplace=True)
    data = df_str.to_dict('records')
    return data
