
Untuk dokumentasi lengkap dalam bahasa Indonesia, silakan kunjungi [README.md dalam Bahasa Indonesia](./README-ID.md).
---

# Diffie-Hellman Performance Evaluation

This repository contains an implementation of a performance evaluation system for Diffie-Hellman using two cryptographic algorithms: **Elliptic Curve Cryptography (ECC)** and **ElGamal (approximated with RSA)**. The system is built using Python and demonstrates key generation, encryption, decryption, and shared key computation using both algorithms.

## Features
- **ECC Key Exchange**: Uses the SECP256R1 curve to generate keys and compute the shared secret.
- **ElGamal Simulation**: Uses RSA for encryption and decryption as an approximation of ElGamal performance.
- **Performance Measurement**: Measures the computation time for ECC and RSA operations based on the average of 100 samples at specific data sizes (50, 100, and 150 bytes).
- **Socket Programming**: Facilitates communication between the server and client for public key exchange.

## System Requirements
- Python 3.9 or higher
- Required Python libraries:
  - `cryptography`

To install the required libraries, run:
```bash
pip install cryptography
```

## How It Works
### Server
The server generates ECC and RSA keys, then sends the public keys to the client. Upon receiving the public key from the client, the server computes the shared key for ECC and simulates RSA operations (encryption and decryption). The server also records the test results and sends them to the client for display.

### Client
The client receives the ECC and RSA public keys from the server, then generates its own ECC and RSA keys and sends the public keys back to the server. The client also computes the shared key for ECC and simulates RSA operations. The test results from the server are displayed in a table format.

## Testing
Testing is conducted for data sizes:
- **50 bytes**
- **100 bytes**
- **150 bytes**

### Measured Parameters
1. **Communication Delay**:
   - The time taken to send and receive data between the server and client.
2. **Computation Delay**:
   - The time taken to compute public keys and shared keys for ECC and RSA.

### Sample Test Results
| **Data Size (bytes)** | **ECC Avg Time (s)** | **RSA Avg Time (s)** |
|-----------------------|----------------------|----------------------|
| 50                    | 0.001234             | 0.002345             |
| 100                   | 0.001456             | 0.002567             |
| 150                   | 0.001678             | 0.002789             |

## Files
- `server.py`: Server-side implementation.
- `client.py`: Client-side implementation.
- `README.md`: This documentation.

## How to Run
1. Start the server:
   ```bash
   python server.py
   ```
2. Start the client:
   ```bash
   python client.py
   ```
3. Observe the results in the terminal:
   - **Server**: Displays process logs and sends performance results to the client.
   - **Client**: Displays the performance results received from the server in a table format.

## Example Output
### Server
```plaintext
[SERVER] --- Performance Results ---
Data Size     ECC Avg Time (s)     RSA Avg Time (s)
----------------------------------------------------
50            0.001234             0.002345
100           0.001456             0.002567
150           0.001678             0.002789
----------------------------------------------------
[SERVER] Performance results have been sent to the client.
```

### Client
```plaintext
[CLIENT] --- Performance Results from Server ---
Data Size     ECC Avg Time (s)     RSA Avg Time (s)
----------------------------------------------------
50            0.001234             0.002345
100           0.001456             0.002567
150           0.001678             0.002789
----------------------------------------------------
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
[Aldil Bhaskoro Anggito Isdwihardjo](https://github.com/aldilbhaskoro)

--- 
