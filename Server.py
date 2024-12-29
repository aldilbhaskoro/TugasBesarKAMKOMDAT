# Server Code
import socket
from time import time, sleep
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.hazmat.primitives import serialization
import base64

# Helper function to measure delays
def measure_computation_time(func, *args):
    start_time = time()
    result = func(*args)
    computation_time = time() - start_time
    return result, computation_time

# Configure socket
HOST = 'localhost'
PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("[SERVER] Waiting for connection...")
conn, addr = server.accept()
print(f"[SERVER] Connection established with {addr}\n")

# ECC Key Generation
print("[SERVER] Generating ECC keys...")
private_key_ecc = ec.generate_private_key(ec.SECP256R1())
public_key_ecc = private_key_ecc.public_key()
public_key_ecc_bytes = public_key_ecc.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# ElGamal (RSA) Key Generation
print("[SERVER] Generating RSA keys (ElGamal equivalent)...")
private_key_rsa = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key_rsa = private_key_rsa.public_key()
public_key_rsa_bytes = public_key_rsa.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Send ECC and RSA public keys to client
print("[SERVER] Sending ECC public key to client...")
conn.sendall(public_key_ecc_bytes)
sleep(0.1)
print("[SERVER] Sending RSA public key to client...\n")
conn.sendall(public_key_rsa_bytes)

# Receive client's ECC and RSA public keys
client_public_key_ecc_bytes = conn.recv(1024)
print("[SERVER] Received client's ECC public key.")
client_public_key_ecc = serialization.load_pem_public_key(client_public_key_ecc_bytes)

client_public_key_rsa_bytes = conn.recv(1024)
print("[SERVER] Received client's RSA public key.\n")
client_public_key_rsa = serialization.load_pem_public_key(client_public_key_rsa_bytes)

# Calculate ECC shared key
_, ecc_computation_time = measure_computation_time(private_key_ecc.exchange, ec.ECDH(), client_public_key_ecc)

# Calculate RSA shared key (dummy decryption for simulation)
dummy_data = base64.b64encode(b"test data")
_, rsa_computation_time = measure_computation_time(private_key_rsa.decrypt, dummy_data)

# Display results
print("[SERVER] --- Performance Results ---")
print(f"ECC Computation Time: {ecc_computation_time:.6f} seconds")
print(f"RSA (ElGamal Approximation) Computation Time: {rsa_computation_time:.6f} seconds")
print("------------------------------------\n")

# Close connection
conn.close()
server.close()
