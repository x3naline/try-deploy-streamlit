import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Aplikasi Visualisasi Data Tanamin 🌱")
st.write("Selamat datang di aplikasi visualisasi data lingkungan!")

data = pd.DataFrame(data={
    "Kampanye": ["Mangrove Balikpapan", "Pantai Samboja", "Delta Mahakam"],
    "Total Donasi (juta)": [120, 85, 60]
})

st.subheader("📈 Data Donasi Kampanye Lingkungan")
st.dataframe(data)

# bar chart
st.bar_chart(data.set_index("Kampanye"))

# line chart
st.line_chart(data.set_index("Kampanye"))

# Matplotlib
fig, ax = plt.subplots()
ax.bar(data["Kampanye"], data["Total Donasi (juta)"], color="red")
ax.set_ylabel("Donasi (juta)")
st.pyplot(fig)

# dropdown menu
tipe = st.selectbox("Pilih jenis grafik:", ["Bar", "Pie", "Line", "doughnut"])

if tipe == "Bar":
    st.bar_chart(data.set_index("Kampanye"))
elif tipe == "Line":
    st.line_chart(data.set_index("Kampanye"))
else:
    fig, ax = plt.subplots()
    ax.pie(data["Total Donasi (juta)"], labels=data["Kampanye"], autopct="%1.1f%%")
    st.pyplot(fig)

# else:
#     fig, ax = plt.subplots()
#     ax.pie(data["Total Donasi (juta)"], labels=data["Kampanye"], autopct="%1.1f%%")
#     st.pyplot(fig)


# slider filter
nilai = st.slider("Tampilkan data dengan donasi minimum:", 0, 150, 50)
st.dataframe(data[data["Total Donasi (juta)"] >= nilai])


# visualisasi geospatial
st.title("Sebaran Lokasi Penanaman Mangrove 🌿")

data_peta = pd.DataFrame({
    'lokasi': ['Balikpapan', 'Samboja', 'Mahakam'],
    'lat': [-1.27, -1.10, -0.50],
    'lon': [116.83, 117.00, 117.25]
})

st.map(data_peta)


# dashboard sederhana
st.title("Dashboard Donasi Lingkungan 🌱")

data = pd.DataFrame({
    "Kampanye": ["Mangrove Balikpapan", "Pantai Samboja", "Delta Mahakam"],
    "Donasi": [120, 85, 60],
    "Target": [150, 100, 90]
})

st.image("mangrove.jpg", caption="Kegiatan Penanaman Mangrove di Balikpapan")
st.markdown("""
### Tujuan Program
Meningkatkan kesadaran masyarakat terhadap pentingnya ekosistem mangrove.
""")

kampanye = st.selectbox("Pilih kampanye:", data["Kampanye"])
row = data[data["Kampanye"] == kampanye].iloc[0]

st.metric("Donasi Saat Ini", f"{row['Donasi']} juta", delta=row['Donasi'] - row['Target'])
st.progress(row['Donasi'] / row['Target'])

fig, ax = plt.subplots()
ax.bar(data["Kampanye"], data["Donasi"], color="green")
ax.set_ylabel("Donasi (juta)")
st.pyplot(fig)