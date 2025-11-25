# Tugas Visualisasi Data dengan Streamlit

## Nama: Khanza Nabila Tsabita
## Nim: 10231049

### 1. Membuat folder
##### Buat folder dengan struktur dibawah dengan nama sesuai dengan preferensi masing - masing
```
project/
└── app1.py
```

### 2. Instalasi Library 
##### Dalam folder yang sudah kita buat, jalankan perintah di bawah didalam aplikasi Visual Studio Code di terminalnya
```
pip install streamlit pandas matplotlib seaborn plotly
```
##### Library yang digunakan mencakup:
1. streamlit : untuk membuat aplikasi web
2. pandas : untuk memanipulasi data
3. matplotlib/plotly : untuk memvisualisasi
4. seaborn : untuk menstyling tambahan (opsional)

##### Lalu cek dengan perintah di bawah untuk mengetahui bahwa instalasi berhasil
```
streamlit hello
```

### 3. Isi file app1.py
##### Setelah berhasil, isi file `app1,py` dengan mengimport modul terlebih dahulu dan membuat judul dan deskripsi dari yang akan di visualisasikan
```
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("📊 Visualisasi Data Interaktif")
st.write("Sistem ini menampilkan berbagai visualisasi dari dataset sederhana.")
st.write("Nama: Khanza Nabila Tsabita | NIM: 10231049 | Kelas: Administraasi Bisnis Data A")
```

##### Setelah mengisi file dari app1.py dengan baris kode diatas, pastikan terminal Visual Studio Code kalian berada di _(visualisasi)_, jika belum maka jalankan perintah dibawah

```
conda activate visualisasi
```

##### Jika sudah berada di _(visualisasi)_, lanjutkan dengan menjalankan kode
```
streamlit run app1.py
```
##### Maka sistem akan mengarahkan dari terminal vscode ke link streamlit yang sudah dijalankan, website yang dijalankan akan menampilkan judul dan deskripsi yang sudah kita buat

### 4. Isi file app1.py dengan data
##### deskripsinya apa ya
```
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
```
##### deskripsinya apa ya
```
st.subheader("📁 Dataset")
st.dataframe(data)
```

### 5. Isi file app1.py dengan dropdown untuk memilih jenis grafik
##### deskripsinya apa ya
```
st.subheader("🔍 Pilih Jenis Grafik")
chart_type = st.selectbox(
    "Pilih Jenis Grafik:",
    ["Bar Chart", "Line Chart", "Area Chart", "Pie Chart", "Map"]
)
```
### 6. Isi file app1.py dengan bar chart, line chart, area chart, pie chart, map chart
##### 6.1 deskripsinya apa ya untuk penjelasan kode bar chart
```
if chart_type == "Bar Chart":
    st.subheader(" 📊 Jumlah Penumpang per Kota")
    fig = px.bar(data, x="Kota", y="Jumlah Penumpang")
    st.plotly_chart(fig)
```
##### 6.2 deskripsinya apa ya untuk penjelasan kode line chart
```
elif chart_type == "Line Chart":
    st.subheader(" 📈 Jumlah Penerbangan per Kota")
    fig = px.line(data, x="Kota", y="Jumlah Penerbangan")
    st.plotly_chart(fig)
```
##### 6.3 deskripsinya apa ya untuk penjelasan kode area chart
```
elif chart_type == "Area Chart":
    st.subheader(" 👥 Tren Jumlah Penumpang")
    fig = px.area(data, x="Kota", y="Jumlah Penumpang")
    st.plotly_chart(fig)
```
##### 6.4 deskripsinya apa ya untuk penjelasan kode pie chart
```
elif chart_type == "Pie Chart":
    st.subheader(" 🌆 Proporsi Penerbangan per Kota")
    fig = px.pie(data, values="Jumlah Penerbangan", names="Kota")
    st.plotly_chart(fig)
```
##### 6.5 deskripsinya apa ya untuk penjelasan kode map
```
elif chart_type == "Map":
    st.subheader(" 🗺️ Peta Sebaran Destinasi Penerbangan")
    st.map(data.rename(columns={"Lat": "lat", "Lon": "lon"}))
```
### 7. Isi file app1.py dengan slider filter
##### 7.1 deskripsinya apa ya untuk penjelasan kode slider memfilter jumlah penerbangan
```
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
```
##### 7.2 deskripsinya apa ya untuk penjelasan kode slider memfilter jumlah penumpang
```
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
```
### 8. Isi file app1.py dengan dambar dan deskripsinya
##### deskripsinya apa ya
```
st.image("plane.jpg", caption="Destinasi Penerbangan yang Paling Sering Dikunjungi ✈️")
st.markdown("""
### 📌 Deskripsi
Sistem ini memvisualisasikan 10 kota di Indonesia dengan aktivitas penerbangan tertinggi. Data ini mencakup informasi tentang aktivitas penerbangan di berbagai kota di Indonesia yang mencakup jumlah penerbangan dan penumpang untuk setiap kota. Visualisasi data yang interaktif ini memungkinkan pengguna untuk memilih jenis visualisasi yang diinginkan, seperti bar chart, line chart, area chart, pie chart, dan peta. 
""")
```
### 9. deploy ke streamlit
##### 9.1 Membuat repository baru di github dengan nama repository sesuai preferensi masing - masing
##### 9.2 Jalankan perintah dibawah untuk upload file ke GitHub
```
git init
git add .
git commit -m "first commit"
git branchh -M main
git remote add origin https://github.com/x3naline/try-deploy-streamlit.git _(link repository kalian)_
git push -u origin main
```
##### 9.3 