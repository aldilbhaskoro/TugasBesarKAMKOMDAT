# Evaluasi Performa Diffie-Hellman

Repository ini berisi implementasi sistem evaluasi performa Diffie-Hellman menggunakan dua algoritma kriptografi: **Elliptic Curve Cryptography (ECC)** dan **ElGamal (diaproksimasi dengan RSA)**. Sistem ini dibuat menggunakan Python dan mendemonstrasikan pembuatan kunci, enkripsi, dekripsi, serta perhitungan shared key menggunakan kedua algoritma.

## Fitur
- **Pertukaran Kunci ECC**: Menggunakan kurva SECP256R1 untuk menghasilkan kunci dan menghitung shared secret.
- **Simulasi ElGamal**: Menggunakan RSA untuk enkripsi dan dekripsi sebagai aproksimasi performa ElGamal.
- **Pengukuran Performa**: Mengukur waktu komputasi untuk operasi ECC dan RSA dengan rata-rata dari 100 sampel.
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
Server menghasilkan kunci ECC dan RSA, kemudian mengirimkan kunci publik ke client. Setelah menerima kunci publik dari client, server menghitung shared key untuk ECC dan mensimulasikan operasi RSA (enkripsi dan dekripsi).

### Client
Client menerima kunci publik ECC dan RSA dari server, kemudian menghasilkan kunci ECC dan RSA miliknya sendiri dan mengirimkan kunci publik kembali ke server. Client juga menghitung shared key untuk ECC dan mensimulasikan operasi RSA.

## File
- `Server.py`: Implementasi sisi server.
- `Client.py`: Implementasi sisi client.
- `README.md`: Dokumentasi ini.

## Cara Menjalankan
1. Jalankan server:
   ```bash
   python Server.py
   ```
2. Jalankan client:
   ```bash
   python Client.py
   ```
3. Amati hasil di terminal, termasuk waktu komputasi untuk ECC dan RSA.

## Contoh Output
### Server
```plaintext
[SERVER] Waiting for connection...
[SERVER] Connection established with ('127.0.0.1', 59105)

[SERVER] Generating ECC keys...
[SERVER] Generating RSA keys (ElGamal equivalent)...
[SERVER] Sending ECC public key to client...
[SERVER] Sending RSA public key to client...

[SERVER] Received client's ECC public key.
[SERVER] Received client's RSA public key.

[SERVER] Encrypting data with RSA public key...
[SERVER] Decrypting data with RSA private key...

[SERVER] --- Performance Results ---
ECC Computation Time: 0.002345 seconds
RSA (ElGamal Approximation) Computation Time: 0.005678 seconds
------------------------------------
```

### Client
```plaintext
[CLIENT] Received server's ECC public key.
[CLIENT] Received server's RSA public key.

[CLIENT] Generating ECC keys...
[CLIENT] Generating RSA keys (ElGamal equivalent)...
[CLIENT] Sending ECC public key to server...
[CLIENT] Sending RSA public key to server...

[CLIENT] Encrypting data with RSA public key...
[CLIENT] Decrypting data with RSA private key...

[CLIENT] --- Performance Results ---
ECC Computation Time: 0.002012 seconds
RSA (ElGamal Approximation) Computation Time: 0.006123 seconds
------------------------------------
```

## Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat file LICENSE untuk detailnya.

## Penulis
[Aldil Bhaskoro Anggito Isdwihardjo](https://github.com/aldilbhaskoro)
