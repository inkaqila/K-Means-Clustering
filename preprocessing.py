import pandas as pd

# Baca file CSV asli
df = pd.read_csv('dataset/Survei_Medsos.csv')

print("\n=== SEBELUM BERSIH ===")
print(f"Jumlah data awal: {len(df)}")
print("Kolom:", list(df.columns))

# Tampilkan nilai unik dari kolom yang akan di-mapping
kolom_mapping_kategorikal = ['Sering', 'Lupa_Waktu', 'Waktu_Sekali_Pakai', 'Waktu_Harian']
for col in kolom_mapping_kategorikal:
    print(f"\nNilai unik di kolom {col}: {df[col].unique()}")

# Mapping platform ke angka
platform_map = {
    'Instagram': 1,
    'WA': 2,
    'LINE': 3,
    'Twitter': 4,
    'Facebook': 5
}

# Mapping durasi ke angka (bisa disesuaikan tergantung skala)
durasi_map = {
    '< 5 menit': 1,
    '5-10 menit': 2,
    '11-30 menit': 3,
    '31-60 menit': 4,
    '1 jam': 4,
    '> 1 jam': 5,
    '2 jam': 5,
    '> 2 jam': 6,
    '3 jam': 6,
    '> 3 jam': 7
}

# Mapping untuk biner
ya_tidak_map = {
    'Ya': 1, 'ya': 1,
    'Pernah': 1,
    'Tidak': 0, 'tidak': 0,
    'Tidak Pernah': 0,
    'Tidak Pernah ': 0,
    'Tidak ': 0,
    'Tdk': 0,
    '': 0
}

# Terapkan mapping kategorikal
df['Sering'] = df['Sering'].map(platform_map)
df['Lupa_Waktu'] = df['Lupa_Waktu'].map(platform_map)
df['Waktu_Sekali_Pakai'] = df['Waktu_Sekali_Pakai'].map(durasi_map)
df['Waktu_Harian'] = df['Waktu_Harian'].map(durasi_map)

# Kolom biner
biner_cols = ['Mengganggu_Produktivitas', 'Membuang_Waktu', 'Tidak_Bisa_Kontrol_Diri',
              'Tidak_Sadar_Waktu', 'Fomo', 'Tanpa_Tujuan', 'Terpikirkan',
              'Usaha_Melepaskan_Diri', 'Kesulitan_Melepaskan_Diri', 'Butuh_Aplikasi',
              'Pernah_Memakai_Aplikasi_Pengaturan_Waktu']

# Bersihkan dan mapping kolom biner
for col in biner_cols:
    df[col] = df[col].astype(str).str.strip().map(ya_tidak_map)

# Tampilkan jumlah NaN per kolom setelah mapping
print("\nJumlah NaN per kolom setelah mapping:")
print(df.isna().sum())

# Buang baris yang mengandung NaN
df = df.dropna()

# Pilih hanya kolom penting
kolom_final = ['Sering', 'Lupa_Waktu', 'Waktu_Sekali_Pakai', 'Waktu_Harian'] + biner_cols
df_bersih = df[kolom_final]

# Cetak hasil akhir
print("\n=== SESUDAH BERSIH ===")
print(f"Jumlah data akhir: {len(df_bersih)}")
print("\n5 Baris Pertama Hasil Bersih:")
print(df_bersih.head())

# Simpan hasil ke CSV
df_bersih.to_csv('dataset/data_bersih.csv', index=False)
