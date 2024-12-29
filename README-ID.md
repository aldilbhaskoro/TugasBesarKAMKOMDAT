---

# Evaluasi Performa Diffie-Hellman

Repository ini berisi implementasi sistem evaluasi performa Diffie-Hellman menggunakan dua algoritma kriptografi: **Elliptic Curve Cryptography (ECC)** dan **ElGamal (diaproksimasi dengan RSA)**. Sistem ini dibuat menggunakan Python dan mendemonstrasikan pembuatan kunci, enkripsi, dekripsi, serta perhitungan shared key menggunakan kedua algoritma.

## Fitur
- **Pertukaran Kunci ECC**: Menggunakan kurva SECP256R1 untuk menghasilkan kunci dan menghitung shared secret.
- **Simulasi ElGamal**: Menggunakan RSA untuk enkripsi dan dekripsi sebagai aproksimasi performa ElGamal.
- **Pengukuran Performa**: Mengukur waktu komputasi untuk operasi ECC dan RSA dengan rata-rata dari 100 sampel pada ukuran data tertentu (50, 100, dan 150 byte).
- **Pemrograman Socket**: Memfasilitasi komunikasi antara server dan client untuk pertukaran kunci publik.

## Kebutuhan Sistem
- Python 3.9 atau lebih tinggi
- Library Python yang dibutuhkan:
  - `cryptography`

Untuk menginstal library yang dibutuhkan, jalankan:
```bash
pip install cryptography
```

## Cara Kerja
### Server
Server menghasilkan kunci ECC dan RSA, kemudian mengirimkan kunci publik ke client. Setelah menerima kunci publik dari client, server menghitung shared key untuk ECC dan mensimulasikan operasi RSA (enkripsi dan dekripsi). Server juga mencatat hasil pengujian dan mengirimkannya ke client untuk ditampilkan.

### Client
Client menerima kunci publik ECC dan RSA dari server, kemudian menghasilkan kunci ECC dan RSA miliknya sendiri dan mengirimkan kunci publik kembali ke server. Client juga menghitung shared key untuk ECC dan mensimulasikan operasi RSA. Hasil pengujian dari server ditampilkan dalam format tabel.

## Pengujian
Pengujian dilakukan untuk ukuran data:
- **50 byte**
- **100 byte**
- **150 byte**

### Parameter yang Diukur
1. **Communication Delay**:
   - Waktu yang dibutuhkan untuk mengirim dan menerima data antara server dan client.
2. **Computation Delay**:
   - Waktu yang dibutuhkan untuk menghitung kunci publik dan shared key untuk ECC dan RSA.

### Contoh Hasil Pengujian
| **Ukuran Data (byte)** | **ECC Avg Time (s)** | **RSA Avg Time (s)** |
|-------------------------|----------------------|-----------------------|
| 50                     | 0.001234            | 0.002345             |
| 100                    | 0.001456            | 0.002567             |
| 150                    | 0.001678            | 0.002789             |

## File
- `server.py`: Implementasi sisi server.
- `client.py`: Implementasi sisi client.
- `README-ID.md`: Dokumentasi ini.


## Cara Menjalankan
1. Jalankan server:
   ```bash
   python server.py
   ```
2. Jalankan client:
   ```bash
   python client.py
   ```
3. Amati hasil di terminal:
   - **Server**: Menampilkan log proses dan mengirim hasil performa ke client.
   - **Client**: Menampilkan hasil performa yang diterima dari server dalam format tabel.

## Contoh Output
### Server
```plaintext
[SERVER] --- Hasil Performa ---
Ukuran Data     ECC Avg Time (s)     RSA Avg Time (s)
-------------------------------------------------------
50              0.001234             0.002345
100             0.001456             0.002567
150             0.001678             0.002789
-------------------------------------------------------
[SERVER] Hasil performa telah dikirim ke client.
```

### Client
```plaintext
[CLIENT] --- Hasil Performa dari Server ---
Ukuran Data     ECC Avg Time (s)     RSA Avg Time (s)
-------------------------------------------------------
50              0.001234             0.002345
100             0.001456             0.002567
150             0.001678             0.002789
-------------------------------------------------------
```

## Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat file LICENSE untuk detailnya.

## Penulis
[Aldil Bhaskoro Anggito Isdwihardjo](https://github.com/aldilbhaskoro)

---
