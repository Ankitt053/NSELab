import hashlib

def hash_file(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

file1 = input("First file: ")
file2 = input("Second file: ")

hash1 = hash_file(file1)
hash2 = hash_file(file2)

print(f"\nHash of {file1}: {hash1}")
print(f"Hash of {file2}: {hash2}")

if hash1 == hash2:
    print("✅ Files are the same!")
else:
    print("❌ Files are different!")
