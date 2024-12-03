# identifikasi library yang akan dipanggil
import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt # impor matplotlib untuk membuat plot

# inisiasi Model
model = pickle.load(open('prediksi_co2.sav','rb')) # open file yang sebelumnya sudah disimpan dengan nama prediksi_co2.sav

# memanggil dataset
df = pd.read_excel('CO2 dataset.xlsx')
# transformasi data Year ke dalam bentuk date time
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index(['Year'], inplace=True)

# membuat judul dari interfacenya
st.title('Forecasting Kualitas Udara')
# untuk menentukan berapa tahun yang akan di forecast
year = st.slider("Tentukan Tahun",1,30, step=1) # (disini batas prediksi yaitu 30 tahun ke depan)

# model prediksi
pred = model.forecast(year)
# menampilakn data frame
pred = pd.DataFrame(pred, columns=['CO2']) 

# membuat tombol untuk mentriger model prediksi
if st.button('Predict'):
    
    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots() 
        df['CO2'].plot(style='--', color='grey', legend=True, label='known') 
        pred['CO2'].plot(color='blue', legend=True, label='Prediction') 
        st.pyplot(fig)
