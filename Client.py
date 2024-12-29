# Client Code
import socket
from time import time, sleep
from cryptography.hazmat.primitives.asymmetric import ec, rsa, padding
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
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Receive server's ECC and RSA public keys
server_public_key_ecc_bytes = client.recv(1024)
print("[CLIENT] Received server's ECC public key.")
server_public_key_ecc = serialization.load_pem_public_key(server_public_key_ecc_bytes)

server_public_key_rsa_bytes = client.recv(1024)
print("[CLIENT] Received server's RSA public key.\n")
server_public_key_rsa = serialization.load_pem_public_key(server_public_key_rsa_bytes)

# ECC Key Generation
print("[CLIENT] Generating ECC keys...")
private_key_ecc = ec.generate_private_key(ec.SECP256R1())
public_key_ecc = private_key_ecc.public_key()
public_key_ecc_bytes = public_key_ecc.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# RSA (ElGamal) Key Generation
print("[CLIENT] Generating RSA keys (ElGamal equivalent)...")
private_key_rsa = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key_rsa = private_key_rsa.public_key()
public_key_rsa_bytes = public_key_rsa.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Send ECC and RSA public keys to server
print("[CLIENT] Sending ECC public key to server...")
client.sendall(public_key_ecc_bytes)
sleep(0.1)
print("[CLIENT] Sending RSA public key to server...\n")
client.sendall(public_key_rsa_bytes)

# Calculate ECC shared key
_, ecc_computation_time = measure_computation_time(private_key_ecc.exchange, ec.ECDH(), server_public_key_ecc)

# Calculate RSA shared key (dummy encryption for simulation)
dummy_data = base64.b64encode(b"test data")
_, rsa_computation_time = measure_computation_time(server_public_key_rsa.encrypt, dummy_data, padding.PKCS1v15())

# Display results
print("[CLIENT] --- Performance Results ---")
print(f"ECC Computation Time: {ecc_computation_time:.6f} seconds")
print(f"RSA (ElGamal Approximation) Computation Time: {rsa_computation_time:.6f} seconds")
print("------------------------------------\n")

# Close connection
client.close()
