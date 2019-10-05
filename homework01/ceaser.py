def encrypt_caesar(s):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    n = 3
    if n >= 26:
        n = n - 26
    if not s:
        return s
    else:
        s = list(s)
        for i in range(0, len(s)):
            s[i] = ord(s[i])
            if (s[i] in range(97, 123 - n) or s[i] in range(65, 91 - n)):
                s[i] = s[i] + n
            elif s[i] in range(91 - n, 91):
                s[i] = s[i] % (91 - n) + 65
            elif s[i] in range(123 - n, 123):
                s[i] = s[i] % (123 - n) + 97
            s[i] = chr(s[i])
        s1 = ''.join(s)
    return s1
# string=input()
# print(encrypt_caesar(string))

def decrypt_caesar(s):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    n = 3
    if n >= 26:
        n = n - 26
    if not s:
        return s
    else:

        s = list(s)
        for i in range(0, len(s)):
            s[i] = ord(s[i])
            if (s[i] in range(97 + n, 123) or s[i] in range(65 + n, 91)):
                s[i] = s[i] - n
            elif s[i] in range(65, 65 + n):
                s[i] = 90 - (65 + n - 1) % s[i]
            elif s[i] in range(97, 97 + n):
                s[i] = 122 - (97 + n - 1) % s[i]
            s[i] = chr(s[i])
        s1 = ''.join(s)
    return s1
# string2=input()
# print(decrypt_caesar(string2))

