import hashlib

# ==============================
# CAESAR CIPHER FUNCTIONS
# ==============================

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# ==============================
# HASHING FUNCTIONS
# ==============================

def hash_text(text, algorithm):
    algo = algorithm.lower()

    if algo == "md5":
        return hashlib.md5(text.encode()).hexdigest()

    elif algo == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()

    elif algo == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()

    else:
        raise ValueError("Unsupported hash algorithm")
