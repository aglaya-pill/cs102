def encrypt_vigenere(text, key):
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    # text = 'ATTACKATDAWN'
    # key = 'LEMON'
    if not text or not key:
        return text
    else:
        key = list(key)
        text = list(text)
        for i in range(0, len(text)):
            if ord(key[i - len(key) * (i // len(key))]) in range(65, 91):
                n = ord(key[i - len(key) * (i // len(key))]) - 65
            elif ord(key[i - len(key) * (i // len(key))]) in range(97, 123):
                n = ord(key[i - len(key) * (i // len(key))]) - 97
            text[i] = ord(text[i])
            if (text[i] in range(97, 123 - n) or text[i] in range(65, 91 - n)):
                text[i] = text[i] + n
            elif text[i] in range(91 - n, 91):
                text[i] = text[i] % (91 - n) + 65
            elif text[i] in range(123 - n, 123):
                text[i] = text[i] % (123 - n) + 97
            text[i] = chr(text[i])
        ciphertext = ''.join(text)
    return ciphertext
t=input()
k=input()
print(encrypt_vigenere(t,k))

def decrypt_vigenere(text, key):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    # text = 'PYTHON'
    # key = 'A'
    if not text or not key:
        return text
    else:
        key = list(key)
        text = list(text)
        for i in range(0, len(text)):
            if ord(key[i - len(key) * (i // len(key))]) in range(65, 91):
                n = ord(key[i - len(key) * (i // len(key))]) - 65
            elif ord(key[i - len(key) * (i // len(key))]) in range(97, 123):
                n = ord(key[i - len(key) * (i // len(key))]) - 97
            text[i] = ord(text[i])
            if (text[i] in range(97 + n, 123) or text[i] in range(65 + n, 91)):
                text[i] = text[i] - n
            elif text[i] in range(65, 65 + n):
                text[i] = 90 - (65 + n - 1) % text[i]
            elif text[i] in range(97, 97 + n):
                text[i] = 122 - (97 + n - 1) % text[i]
            text[i] = chr(text[i])
        plaintext = ''.join(text)
    return plaintext
t=input()
k=input()
print(decrypt_vigenere(t,k))
