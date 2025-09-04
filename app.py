import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic

# -----------------------------
# Fungsi untuk menghitung rute dengan Nearest Neighbor
# -----------------------------
def nearest_neighbor_route(df, start_index=0):
    visited = [start_index]
    unvisited = list(range(len(df)))
    unvisited.remove(start_index)
    current = start_index

    while unvisited:
        nearest = min(unvisited, key=lambda i: geodesic(
            (df.iloc[current]['Latitude'], df.iloc[current]['Longitude']),
            (df.iloc[i]['Latitude'], df.iloc[i]['Longitude'])
        ).km)
        visited.append(nearest)
        unvisited.remove(nearest)
        current = nearest

    return visited


# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="Flight Path Optimization", layout="wide")

st.title("✈️ Flight Path Optimization (Nearest Neighbor)")

# 👉 Petunjuk di awal
# Contoh format CSV
st.write("**Contoh format file CSV yang benar:**")
st.code(
    "City,Latitude,Longitude\n"
    "Jakarta,-6.2088,106.8456\n"
    "Bandung,-6.9175,107.6191\n"
    "Yogyakarta,-7.7956,110.3695",
    language="csv"
)

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Data Asli")
    st.write(df)

    # 🔹 Deteksi otomatis nama kolom
    expected_cols = ["City", "Latitude", "Longitude"]
    col_mapping = {}

    for col in expected_cols:
        if col in df.columns:
            col_mapping[col] = col
        else:
            st.warning(f"Kolom **{col}** tidak ditemukan di file CSV. Silakan pilih kolom yang sesuai.")
            col_mapping[col] = st.selectbox(
                f"Pilih kolom untuk {col}",
                df.columns.tolist(),
                key=f"select_{col}"
            )

    # Gunakan nama kolom sesuai mapping user
    df = df.rename(columns={
        col_mapping["City"]: "City",
        col_mapping["Latitude"]: "Latitude",
        col_mapping["Longitude"]: "Longitude"
    })

    # 🔹 Pilih titik start
    start_city = st.selectbox("🏁 Pilih Kota Awal:", df['City'].tolist())
    start_index = df[df['City'] == start_city].index[0]

    # 🔹 Hitung rute
    route_order = nearest_neighbor_route(df, start_index=start_index)
    ordered_df = df.iloc[route_order].reset_index(drop=True)

    st.subheader("📍 Urutan Rute")
    st.write(ordered_df)

    # 🔹 Visualisasi Peta
    start_coords = (ordered_df.iloc[0]['Latitude'], ordered_df.iloc[0]['Longitude'])
    m = folium.Map(location=start_coords, zoom_start=6)

    for i, row in ordered_df.iterrows():
        popup_text = f"{i+1}. {row['City']}"
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=popup_text,
            tooltip=popup_text,
            icon=folium.Icon(color="blue" if i > 0 else "red", icon="info-sign")
        ).add_to(m)

    folium.PolyLine(
        locations=ordered_df[['Latitude', 'Longitude']].values.tolist(),
        color="blue", weight=2.5, opacity=1
    ).add_to(m)

    st.subheader("🗺️ Visualisasi Peta")
    st_folium(m, width=800, height=500)
