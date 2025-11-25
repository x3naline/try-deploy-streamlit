import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Visualisasi Data Interaktif")
st.write("Sistem ini menampilkan berbagai visualisasi dari dataset sederhana.")
st.write("Nama: Khanza Nabila Tsabita | NIM: 10231049 | Kelas: Administraasi Bisnis Data A")

# gambar
st.image("plane.jpg", caption="Destinasi Penerbangan yang Paling Sering Dikunjungi ✈️")
st.markdown("""
### 📌 Deskripsi
Sistem ini memvisualisasikan 10 kota di Indonesia dengan aktivitas penerbangan tertinggi. Data ini mencakup informasi tentang aktivitas penerbangan di berbagai kota di Indonesia yang mencakup jumlah penerbangan dan penumpang untuk setiap kota. Visualisasi data yang interaktif ini memungkinkan pengguna untuk memilih jenis visualisasi yang diinginkan, seperti bar chart, line chart, area chart, pie chart, dan peta. 
""")

# dataset
data = pd.DataFrame({
    "Kota": [
        "Jakarta", "Surabaya", "Denpasar", "Makassar", "Medan",
        "Balikpapan", "Yogyakarta", "Manado", "Palembang", "Lombok"
    ],
    "Jumlah Penerbangan": [320, 280, 260, 240, 210, 195, 180, 165, 150, 140],
    "Jumlah Penumpang": [520000, 450000, 430000, 390000, 350000, 300000, 280000, 255000, 230000, 210000],
    "Lat": [-6.2, -7.2, -8.6, -5.1, 3.6, -1.2, -7.8, 1.4, -2.9, -8.7],
    "Lon": [106.8, 112.7, 115.2, 119.4, 98.7, 116.8, 110.4, 124.8, 104.7, 116.1]
})


st.subheader("📁 Dataset")
st.dataframe(data)


# dropdown menu untuk memilih jenis grafik
st.subheader("🔍 Pilih Jenis Grafik")
chart_type = st.selectbox(
    "Pilih Jenis Grafik:",
    ["Bar Chart", "Line Chart", "Area Chart", "Pie Chart", "Map"]
)

if chart_type == "Bar Chart":
    st.subheader(" 📊 Jumlah Penumpang per Kota")
    fig = px.bar(data, x="Kota", y="Jumlah Penumpang")
    st.plotly_chart(fig)

elif chart_type == "Line Chart":
    st.subheader(" 📈 Jumlah Penerbangan per Kota")
    fig = px.line(data, x="Kota", y="Jumlah Penerbangan")
    st.plotly_chart(fig)

elif chart_type == "Area Chart":
    st.subheader(" 👥 Tren Jumlah Penumpang")
    fig = px.area(data, x="Kota", y="Jumlah Penumpang")
    st.plotly_chart(fig)

elif chart_type == "Pie Chart":
    st.subheader(" 🌆 Proporsi Penerbangan per Kota")
    fig = px.pie(data, values="Jumlah Penerbangan", names="Kota")
    st.plotly_chart(fig)

elif chart_type == "Map":
    st.subheader(" 🗺️ Peta Sebaran Destinasi Penerbangan")
    st.map(data.rename(columns={"Lat": "lat", "Lon": "lon"}))


# Slider filter untuk jumlah penerbangan
st.subheader("🔍 Filter untuk jumlah penerbangan")
min_flights = st.slider(
    "Tampilkan kota dengan jumlah penerbangan minimum:",
    min_value=0,
    max_value=int(data["Jumlah Penerbangan"].max()),
    value=150
)

filtered_data = data[data["Jumlah Penerbangan"] >= min_flights]

st.subheader("📋 Data Setelah Filter")
st.dataframe(filtered_data)
st.write("Jumlah Kota:", len(filtered_data))

# Slider filter untuk jumlah penumpang
st.subheader("🔍 Filter untuk jumlah penumpang")
min_passengers = st.slider(
    "Tampilkan kota dengan jumlah penumpang minimum:",
    min_value=0,
    max_value=int(data["Jumlah Penumpang"].max()),
    value=250000
)

filtered_data = data[data["Jumlah Penumpang"] >= min_passengers]

st.subheader("📋 Data Setelah Filter")
st.dataframe(filtered_data)
st.write("Jumlah Kota:", len(filtered_data))
