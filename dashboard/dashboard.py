import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style="dark")

# Dashboard Title
st.title("Bike-Sharing-Dataset-Dashboard 🚴")


# Fungsi untuk membuat data agregasi
def create_total_count_byday_df(day_df):
  total_count_byday_df = day_df.groupby(by = ["weekday"], observed = True)["count"].sum()
  return total_count_byday_df

def create_total_count_byhour_df(hour_df):
    total_count_byhour_df= hour_df.groupby(by = ["hours"], observed = True)["count"].sum()
    return total_count_byhour_df

def create_total_registered_df(day_df):
   registered_df =  day_df.groupby(by="date_day").agg({
      "registered": "sum"
    })
   registered_df = registered_df.reset_index()
   registered_df.rename(columns={
        "registered": "register_sum"
    }, inplace=True)
   return registered_df

def create_total_casual_df(day_df):
   casual_df = day_df.groupby(by="date_day")["casual"].sum().reset_index()
   casual_df = casual_df.reset_index()
   casual_df.rename(columns={
        "casual": "casual_sum"
    }, inplace=True)
   return casual_df


# Membaca data dari file csv
days_df = pd.read_csv("day_upgrade.csv")
hours_df = pd.read_csv("hour_upgrade.csv")


# Konversi kolom tanggal ke format datetime
days_df["date_day"] = pd.to_datetime(days_df["date_day"])
hours_df["date_day"] = pd.to_datetime(hours_df["date_day"])


# Definisi bins dan label untuk kategori waktu
bins = [0, 6, 12, 18, 24]
labels = ["Dini Hari (00.00-05.59)", "Pagi (06.00-11.59)", "Siang-Sore (12.00-17.59)", "Malam (18.00-23.59)"]


# Terapkan binning pada kolom 'hours'
hours_df["kategori_waktu"] = pd.cut(hours_df["hours"], bins=bins, labels=labels, include_lowest=True, right=False)


# Komponen Sidebar Filter
with st.sidebar:
    st.header("🔍 Pencarian")
    start_date, end_date = st.date_input("Rentang Waktu", [days_df["date_day"].min(), days_df["date_day"].max()])
    selected_season = st.multiselect("Pilih Musim:", options=days_df["season"].unique(), default=days_df["season"].unique())
    selected_weather = st.multiselect("Pilih Kondisi Cuaca:", options=days_df["weathersit"].unique(), default=days_df["weathersit"].unique())
    selected_time_range = st.multiselect("Pilih Rentang Waktu:", options=labels, default=labels)


# Filter Data untuk Tabel
start_date, end_date = pd.to_datetime(start_date), pd.to_datetime(end_date)
filtered_df_days = days_df[(days_df["date_day"] >= start_date) & (days_df["date_day"] <= end_date) &
                           (days_df["season"].isin(selected_season)) & (days_df["weathersit"].isin(selected_weather))]

filtered_df_hours = hours_df[(hours_df["date_day"] >= start_date) & (hours_df["date_day"] <= end_date) &
                             (hours_df["season"].isin(selected_season)) & (hours_df["weathersit"].isin(selected_weather))]


# Filter berdasarkan rentang waktu
filtered_df_hours = filtered_df_hours[filtered_df_hours["kategori_waktu"].isin(selected_time_range)]

# Metrics Display
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=filtered_df_days["count"].sum())
with col2:
    st.metric("Member", value=filtered_df_days["registered"].sum())
with col3:
    st.metric("Non Member", value=filtered_df_days["casual"].sum())


# Menampilkan Tabel Data Penyewaan Sepeda yang Difilter
st.subheader("Data Penyewaan Sepeda yang telah difilter")
st.write(filtered_df_days)
st.subheader("Data Penyewaan Sepeda yang telah difilter (Per kategori waktu)")
st.write(filtered_df_hours)

# Menampilkan bar chart jumlah penyewaan sepeda berdasarkan kategori waktu 
st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Kategori Waktu")
waktu_grouped = hours_df.groupby("kategori_waktu", observed=True)["count"].sum().astype(int).reset_index()
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="kategori_waktu", y="count", data=waktu_grouped, color="mediumpurple", ax=ax)
ax.set_xlabel("Kategori Waktu")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
plt.xticks(rotation=45)
st.pyplot(fig)

## Menampilkan diagram Performa penyewaan sepeda dalam beberapa tahun terakhir
st.subheader("Performa penyewaan sepeda dalam beberapa tahun terakhir")
fig, ax = plt.subplots(figsize=(20,10))
ax.plot(
   days_df["date_day"],
   days_df["count"],
   marker='o',
   markerfacecolor="red",
   linewidth = 1,
   color = "blue"
)
ax.tick_params(axis='y',labelsize=20)
ax.tick_params(axis='x',labelsize=20)
st.pyplot(fig)


## Menampilkan diagram Jumlah penyewaan sepeda berdasarkan musim

# Mengatur warna untuk masing-masing bar chart
colors1 = ["darkorange","burlywood", "burlywood","burlywood"]
colors2 = ["peachpuff", "peachpuff", "salmon","peachpuff"]
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 10)) 
sns.barplot(
    y ="count", 
    x ="season",
    hue ="season",
    data = days_df.sort_values(by="season", ascending=True),
    palette = colors1,
    errorbar = None,
    ax = axes[0] 
)
axes[0].set_title("Grafik Penyewaan Sepeda Berdasarkan Musim Tertinggi", fontsize=20)
axes[0].set_ylabel("Jumlah penyewa sepeda", fontsize = 20)
axes[0].set_xlabel("Musim", fontsize = 20)
axes[0].tick_params(axis ='x', labelsize = 20)
axes[0].tick_params(axis ='y', labelsize = 20)
sns.barplot(
    y ="count", 
    x ="season",
    hue ="season",
    data = days_df.sort_values(by="season", ascending=False),
    palette = colors2,
    errorbar = None,
    ax = axes[1]  
)
axes[1].set_title("Grafik Penyewaan Sepeda Berdasarkan Musim Terendah", fontsize=20)
axes[1].set_ylabel("Jumlah penyewa sepeda", fontsize = 20)
axes[1].set_xlabel("Musim", fontsize = 20)
axes[1].tick_params(axis ='x', labelsize= 20)
axes[1].tick_params(axis ='y', labelsize= 20)
st.pyplot(fig)


## Menampilkan jumlah penyewaan sepeda pada Hari Libur vs Hari Kerja
st.subheader("Jumlah Penyewaan sepeda pada Hari Libur vs Hari Kerja")
colors = ["#90CAF9","#1f77b4"]
total_workingday = days_df.groupby(by = ["workingday"], observed = True, as_index=False)["count"].sum()
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
        y ="count", 
        x ="workingday",
        hue ="workingday",
        data = total_workingday,
        palette = colors,
        errorbar = None,
        ax = ax
    )
ax.set_title("Hari Libur vs Hari Kerja", loc ="center", fontsize=20)
ax.set_ylabel("Jumlah Penyewa Sepeda", fontsize = 20)
ax.set_xlabel(None)
ax.tick_params(axis ='x', labelsize = 20)
ax.tick_params(axis ='y', labelsize = 20)
st.pyplot(fig)


## Menampilkan diagram Perbandingan pengguna casual dan registered
st.subheader("Perbandingan pengguna casual dan registered")
jumlah_total_casual = sum(days_df['casual'])
jumlah_total_registered = sum(days_df['registered'])
data = [jumlah_total_casual, jumlah_total_registered]
labels = ["Casual (pengguna biasa)", "Registered (pengguna terdaftar)"]
colors=["#E67F0D", "#93C572"]
fig, ax = plt.subplots()
ax.pie(data, 
        labels=labels, 
        autopct='%1.1f%%', 
        colors=colors)
st.pyplot(fig)


## Menampilkan diagram Tren jumlah penyewaan sepeda berdasarkan jam
st.subheader("Tren jumlah penyewaan sepeda berdasarkan jam")
fig, ax = plt.subplots(figsize=(23,9))
hourly_count = hours_df["count"].groupby(hours_df["hours"]).max()
ax.scatter(hourly_count.index, hourly_count.values, color="red", s=50, marker='o')
ax.plot(hourly_count.index, hourly_count.values, color="#1f77b4")
ax.set_xlabel("Jam", fontsize=15)
ax.set_ylabel("jumlah penyewaan sepeda", fontsize=20)
ax.set_title("Grafik Jumlah Penyewa Sepeda Berdasarkan Jam", fontsize=25)
ax.tick_params(axis='x', labelsize=25)
ax.tick_params(axis='y', labelsize=25)
st.pyplot(fig)
