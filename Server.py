# Server Code
import socket
from time import time
from cryptography.hazmat.primitives.asymmetric import ec, rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Helper function to measure computation time
def measure_computation_time(func, *args):
    start_time = time()
    result = func(*args)
    computation_time = time() - start_time
    return result, computation_time

# Helper function to measure communication time
def measure_communication_time(conn, data=None, recv=False):
    start_time = time()
    if recv:
        conn.recv(1024)
    else:
        conn.sendall(data)
    return time() - start_time

# Configure server socket
HOST = 'localhost'
PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("\n[SERVER] Menunggu koneksi dari client...")
conn, addr = server.accept()
print(f"[SERVER] Terhubung ke client di {addr}\n")

# Data sizes to test (in bytes)
data_sizes = [50, 100, 150]

# Lists to store results
ecc_comp_times = {size: [] for size in data_sizes}
rsa_comp_times = {size: [] for size in data_sizes}

# Perform 100 iterations
for iteration in range(100):
    print(f"\n[SERVER] Iterasi {iteration + 1}/100")

    # Generate ECC keys
    private_key_ecc = ec.generate_private_key(ec.SECP256R1())
    public_key_ecc = private_key_ecc.public_key()
    public_key_ecc_bytes = public_key_ecc.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Generate RSA keys
    private_key_rsa = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key_rsa = private_key_rsa.public_key()
    public_key_rsa_bytes = public_key_rsa.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Send public keys to client
    measure_communication_time(conn, data=public_key_ecc_bytes)  # ECC key
    measure_communication_time(conn, data=public_key_rsa_bytes)  # RSA key

    # Receive client's public keys
    client_public_key_ecc_bytes = conn.recv(1024)
    client_public_key_ecc = serialization.load_pem_public_key(client_public_key_ecc_bytes)

    client_public_key_rsa_bytes = conn.recv(1024)
    client_public_key_rsa = serialization.load_pem_public_key(client_public_key_rsa_bytes)

    # Test for each data size
    for size in data_sizes:
        print(f"[SERVER] Mengukur untuk ukuran data: {size} bytes")

        # Generate test data of specified size
        test_data = b'a' * size

        # Compute ECC shared key
        _, ecc_comp_time = measure_computation_time(private_key_ecc.exchange, ec.ECDH(), client_public_key_ecc)
        ecc_comp_times[size].append(ecc_comp_time)

        # Simulate RSA encryption and decryption
        encrypted_data = public_key_rsa.encrypt(
            test_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        _, rsa_comp_time = measure_computation_time(
            private_key_rsa.decrypt,
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        rsa_comp_times[size].append(rsa_comp_time)

# Prepare performance results
results = "\n[SERVER] --- Hasil Performa ---\n"
results += f"{'Ukuran Data':<15}{'ECC Avg Time (s)':<20}{'RSA Avg Time (s)':<20}\n"
results += "-" * 55 + "\n"
for size in data_sizes:
    avg_ecc_comp_time = sum(ecc_comp_times[size]) / len(ecc_comp_times[size])
    avg_rsa_comp_time = sum(rsa_comp_times[size]) / len(rsa_comp_times[size])
    results += f"{size:<15}{avg_ecc_comp_time:<20.6f}{avg_rsa_comp_time:<20.6f}\n"
results += "-" * 55

# Display results in the server terminal
print(results)

# Send results to client
conn.sendall(results.encode('utf-8'))
print("\n[SERVER] Hasil performa telah dikirim ke client.")

# Close the connection
conn.close()
server.close()
