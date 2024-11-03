from cryptography.hazmat.primitives import serialization

# Load the public key from the PEM file
with open("transparency.pem", "rb") as pem_file:
    pem_data = pem_file.read()

# Load the public key
public_key = serialization.load_pem_public_key(pem_data)

# Get the public numbers (n and e)
public_numbers = public_key.public_numbers()
modulus = public_numbers.n
exponent = public_numbers.e

print(f"Modulus (n): {modulus}")
print(f"Public Exponent (e): {exponent}")
