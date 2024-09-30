def encryption(plain_text, key):
    return ''.join(chr((ord(p) + ord(k) - 2 * ord('A')) % 26 + ord('A')) for p, k in zip(plain_text, key))

def decryption(cipher_text, key):
    return ''.join(chr((ord(c) - ord(k) + 26) % 26 + ord('A')) for c, k in zip(cipher_text, key))

# Input for plain text and key
plain_text = input("Enter the plain text: ").upper()
key = input("Enter the key: ").upper()

# Encrypt the plain text
encrypted = encryption(plain_text, key)
print("Encrypted message:", encrypted)

# Decrypt the cipher text
decrypted = decryption(encrypted, key)
print("Decrypted message:", decrypted)
