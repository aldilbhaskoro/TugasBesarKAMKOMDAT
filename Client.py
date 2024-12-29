# Client Code
import socket
from time import time
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.hazmat.primitives import serialization

# Helper function to receive large data
def receive_large_data(conn):
    data = b""
    while True:
        part = conn.recv(1024)
        data += part
        if len(part) < 1024:  # End of transmission
            break
    return data.decode('utf-8')

# Configure client socket
HOST = 'localhost'
PORT = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("\n[CLIENT] Terhubung ke server.\n")

# Data sizes to test (in bytes)
data_sizes = [50, 100, 150]

# Perform 100 iterations
for iteration in range(100):
    print(f"\n[CLIENT] Iterasi {iteration + 1}/100")

    # Receive server's public keys
    server_public_key_ecc_bytes = client.recv(1024)
    server_public_key_ecc = serialization.load_pem_public_key(server_public_key_ecc_bytes)

    server_public_key_rsa_bytes = client.recv(1024)
    server_public_key_rsa = serialization.load_pem_public_key(server_public_key_rsa_bytes)

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

    # Send public keys to server
    client.sendall(public_key_ecc_bytes)  # ECC key
    client.sendall(public_key_rsa_bytes)  # RSA key

# Receive and display performance results from server
print("\n[CLIENT] --- Hasil Performa dari Server ---")
results = receive_large_data(client)
print(results)

# Close the connection
client.close()
