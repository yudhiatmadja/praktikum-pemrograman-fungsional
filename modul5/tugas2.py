import pandas as pd

# 1. Membaca file CSV
df = pd.read_csv('data.csv')


print("10 Data pertama:")
print(df.head(10))


print("\nInformasi umum dataset:")
print(df.info())


df['date'] = pd.to_datetime(df['date'])

df['tahun'] = df['date'].dt.year


rata_rata_per_tahun = df.groupby('tahun')['price'].mean()
print("\nRata-rata harga per tahun:")
print(rata_rata_per_tahun)

harga_tertinggi = df.loc[df['price'].idxmax()]
harga_terendah = df.loc[df['price'].idxmin()]
print("\nProduk dengan harga tertinggi:")
print(harga_tertinggi)
print("\nProduk dengan harga terendah:")
print(harga_terendah)

produk_terfilter = df[(df['price'] >= 1.50) & (df['price'] <= 2.35)]
print("\nProduk dengan harga antara 1.50 dan 2.35:")
print(produk_terfilter)
