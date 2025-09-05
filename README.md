✈️ Flight Path Optimization

Deskripsi :
Project ini adalah aplikasi interaktif untuk optimasi jalur penerbangan (UAV/Drone) menggunakan algoritma Nearest Neighbor.
Aplikasi dibangun dengan Python + Streamlit sehingga dapat dijalankan langsung di browser tanpa perlu setting rumit.

Fitur Utama :
📂 Upload CSV berisi nama kota, latitude, dan longitude.
🗺️ Peta interaktif (Folium + Streamlit).
🚏 Pemilihan titik awal perjalanan.
📜 Visualisasi urutan kota sesuai hasil optimasi.
📑 Output file berupa:
          route_map.html → peta interaktif (dibuka di browser).
          route.png → visualisasi rute statis (gambar).
          
Instalasi :
1. Clone repository atau download ZIP:
   git clone https://github.com/username/flight-path-optimization.git
   cd flight-path-optimization

2. Buat virtual environment (opsional, tapi disarankan):
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

3. Install dependencies:
   pip install -r requirements.txt


Cara Menjalankan Project

Proyek ini bisa dijalankan dengan dua mode:

1. Mode Streamlit (Web App Interaktif)
Menjalankan aplikasi berbasis web.

    streamlit run app.py

Fitur di Streamlit:
Upload file CSV.
Pilih titik awal perjalanan.
Tampilkan rute optimal di peta interaktif.
Lihat urutan kota hasil optimasi.

2. Mode Script (Output HTML & PNG)
Menjalankan script langsung untuk menghasilkan file output (tanpa web app).

    python src/main.py

Setelah dijalankan, file output akan tersimpan di folder output/:
  route_map.html → peta interaktif, bisa dibuka di browser.
  route.png → visualisasi rute dalam format gambar.


📂 Struktur Project

flight-path-optimization/
│
├── app.py                # Streamlit web app
├── requirements.txt      # Daftar dependencies
├── README.md             # Dokumentasi proyek
│
├── src/
│   ├── main.py           # Main script (generate HTML/PNG)
│   ├── utils.py          # Fungsi bantu (baca CSV, hitung jarak)
│   └── visualizer.py     # Fungsi visualisasi peta
│
├── data/
│   └── coordinates_gps.csv   # Contoh data kota (opsional)
│
└── output/
    ├── route_map.html    # Hasil peta interaktif
    └── route.png         # Hasil visualisasi rute

Contoh Data CSV

Pastikan file CSV memiliki kolom berikut:

City → nama kota
Latitude → lintang
Longitude → bujur

Contoh:

City,Latitude,Longitude
Jakarta,-6.2088,106.8456
Bandung,-6.9175,107.6191
Yogyakarta,-7.7956,110.3695
Surabaya,-7.2575,112.7521
Denpasar,-8.65,115.2167


Teknologi yang Digunakan 

Python 3
Streamlit – web app interaktif
Pandas – baca & olah data
Folium – peta interaktif
streamlit-folium – integrasi folium dengan Streamlit

✍️ Author

Muhammad Faiz Al Basit (245060700111040) -- Teknik Industri Universitas Brawijaya Angkatan 2024
