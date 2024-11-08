# picoCTF: Custom Encryption

**Author:** NGIRIMANA Schadrack

## Problem Statement

The challenge involves decrypting a file that has been encrypted using a custom encryption function. You are provided with some encrypted data and a code file that explains how the encryption was done. Your goal is to decode the encrypted content and retrieve the flag.

## Given Data:
- `a = 94`
- `b = 29`
- **Cipher Text:**
  
- `[260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 925536, 1417227, 751998, 202461, 347076, 491691]`

- 
## Code Analysis

The code provided uses a combination of modular exponentiation (generator function), a dynamic XOR encryption scheme, and basic multiplication to encrypt the plaintext.

### Key Insights:
- The `test` function in the code defines the core of the encryption mechanism. It uses the values `a` and `b` to generate a shared key using modular exponentiation.
- The shared key is then used to encrypt the plaintext.
- The encryption is a two-step process: First, XOR encryption is applied to the plaintext, and then the result is multiplied by the shared key to get the final ciphertext.

## Approach

### Step 1: Key Calculation

The shared key is computed using the values of `a` and `b` in the `test` function. The values `a = 94` and `b = 29` are plugged into the `generator` function which uses modular exponentiation to generate the shared key.

- **Shared Key:** After running the code logic, the shared key calculated was `93`.

### Step 2: Decryption Process

#### Decrypting the Cipher:

1. **First Step:** We reverse the multiplication operation (which was applied to each character of the plaintext). The final key used in this multiplication is `key * 311`, where `key = 93`.

 The decryption function divides each encrypted value by the final key and converts it back to characters using `chr()`.

2. **Second Step:** The second part of the encryption involved XORing the plaintext characters with a key (`text_key`). We reverse this operation by XORing the result with the same key used for encryption.

### Step 3: Decryption Code

```python
def decrypt(cipher, key):
  final_key = key * 311  # Reverse the multiplication
  plain_text = ""
  for char in cipher:
      realchar = int(char / final_key)  # Reverse the multiplication
      plain_text += chr(realchar)  # Convert back to character
  return plain_text

def dynamic_xor_decrypt(encrypted_text, text_key):
  decrypted_text = ""
  key_length = len(text_key)
  for i, char in enumerate(encrypted_text):
      key_char = text_key[i % key_length]  # Get key character
      decrypted_char = chr(ord(char) ^ ord(key_char))  # XOR back to original char
      decrypted_text = decrypted_char + decrypted_text  # Reverse the encryption
  return decrypted_text

# Encrypted cipher from the problem
cipher = [260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 925536, 1417227, 751998, 202461, 347076, 491691]
key = 93  # The key calculated from the test function
text_key = "trudeau"

# Step 1: Decrypt the cipher using the shared key
res = decrypt(cipher, key)

# Step 2: Reverse the XOR operation
final = dynamic_xor_decrypt(res, text_key)

print("Decrypted flag:", final)
```

### Output
After running the decryption process, I successfully retrieved the decrypted flag.

**Flag:**

```flag
picoCTF{custom_d2cr0pt6d_751a22dc}
```
