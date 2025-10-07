import string

lower, upper = string.ascii_lowercase, string.ascii_uppercase

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.islower():
            result += lower[(lower.index(char) + shift) % 26]
        elif char.isupper():
            result += upper[(upper.index(char) + shift) % 26]
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    result, j = "", 0
    for char in text:
        if char.isalpha():
            k = lower.index(key[j % len(key)].lower())
            if char.islower():
                result += lower[(lower.index(char) + k) % 26]
            else:
                result += upper[(upper.index(char) + k) % 26]
            j += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result, j = "", 0
    for char in text:
        if char.isalpha():
            k = lower.index(key[j % len(key)].lower())
            if char.islower():
                result += lower[(lower.index(char) - k) % 26]
            else:
                result += upper[(upper.index(char) - k) % 26]
            j += 1
        else:
            result += char
    return result

print("Choose Encryption Method:")
print("1. Caesar Cipher")
print("2. Vigenère Cipher")

choice = input("Enter 1 or 2: ").strip()
message = input("Enter the message: ").strip()

if choice == "1":
    shift = int(input("Enter shift value (e.g., 3): ").strip())
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)
else:
    key = input("Enter key (alphabetic): ").strip()
    encrypted = vigenere_encrypt(message, key)
    decrypted = vigenere_decrypt(encrypted, key)

print("\n--- Result ---")
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
