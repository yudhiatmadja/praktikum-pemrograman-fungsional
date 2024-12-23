from datetime import datetime


data_penjualan = [
    {"id_produk": "GN001", "nama_produk": "Baju", "harga": 100000, "quantity": 2, "tanggal_penjualan": "2024-08-01"},
    {"id_produk": "GN002", "nama_produk": "Celana", "harga": 150000, "quantity": 1, "tanggal_penjualan": "2024-08-01"},
    {"id_produk": "GN003", "nama_produk": "Sepatu", "harga": 200000, "quantity": 3, "tanggal_penjualan": "2024-08-01"},
    
    {"id_produk": "GN004", "nama_produk": "Topi", "harga": 50000, "quantity": 4, "tanggal_penjualan": "2024-08-02"},
    {"id_produk": "GN005", "nama_produk": "Tas", "harga": 175000, "quantity": 2, "tanggal_penjualan": "2024-08-02"},
    {"id_produk": "GN006", "nama_produk": "Jaket", "harga": 250000, "quantity": 1, "tanggal_penjualan": "2024-08-02"},
    
    {"id_produk": "GN007", "nama_produk": "Kemeja", "harga": 120000, "quantity": 3, "tanggal_penjualan": "2024-08-03"},
    {"id_produk": "GN008", "nama_produk": "Jas Hujan", "harga": 90000, "quantity": 2, "tanggal_penjualan": "2024-08-03"},
    {"id_produk": "GN009", "nama_produk": "Kaos", "harga": 60000, "quantity": 5, "tanggal_penjualan": "2024-08-03"},
    
    {"id_produk": "GN010", "nama_produk": "Dompet", "harga": 45000, "quantity": 6, "tanggal_penjualan": "2024-08-04"},
    {"id_produk": "GN011", "nama_produk": "Sarung", "harga": 75000, "quantity": 3, "tanggal_penjualan": "2024-08-04"},
    {"id_produk": "GN012", "nama_produk": "Sandal", "harga": 25000, "quantity": 8, "tanggal_penjualan": "2024-08-04"},
]

def hitung_pendapatan(data):
    return [
        {
            **item,
            "pendapatan": item["harga"] * item["quantity"]
        }
        for item in data
    ]


def average_penjualan(data, tanggal):
    try:

        datetime.strptime(tanggal, '%Y-%m-%d')

        penjualan_per_tanggal = [item['pendapatan'] for item in data if item['tanggal_penjualan'] == tanggal]
        if not penjualan_per_tanggal:
            raise ValueError("Tidak ada penjualan pada tanggal tersebut.")
        
        return sum(penjualan_per_tanggal) / len(penjualan_per_tanggal)
    
    except ValueError as err:
        return str(err)


def total_penjualan(data):
    tanggal_set = set(item['tanggal_penjualan'] for item in data)
    for tanggal in tanggal_set:
        total = sum(item['pendapatan'] for item in data if item['tanggal_penjualan'] == tanggal)
        yield f"Tanggal: {tanggal}, Total Penjualan: {total}"


data_dengan_pendapatan = hitung_pendapatan(data_penjualan)


tanggal_input = input("Masukkan tanggal yang ingin dicari (YYYY-MM-DD): ")
rata_rata = average_penjualan(data_dengan_pendapatan, tanggal_input)

if isinstance(rata_rata, str):
    print(rata_rata)  
else:
    print(f"Rata-rata penjualan pada tanggal {tanggal_input}: Rp{rata_rata:.2f}")

print("\nTotal Penjualan Per Tanggal:")
for total in total_penjualan(data_dengan_pendapatan):
    print(total)
