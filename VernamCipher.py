def Encryption(text, key):
    cipherText = ""
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    cipher = []
    for i in range(len(key)):
        cipher.append((ord(text[i]) - ord('A') + ord(key[i]) - ord('A')) % 26)
    for i in range(len(key)):
        x = cipher[i] + ord('A')
        cipherText += chr(x)
    return cipherText

def Decryption(s, key):
    plainText = ""
    key = key * (len(s) // len(key)) + key[:len(s) % len(key)]
    plain = []
    for i in range(len(key)):
        plain.append((ord(s[i]) - ord('A') - (ord(key[i]) - ord('A'))) % 26)
    for i in range(len(key)):
        x = plain[i] + ord('A')
        plainText += chr(x)
    return plainText


plainText = input("Enter message to be encrypted: ")
key = input("Enter key: ")
encryptedText = Encryption(plainText.upper(), key.upper())
print("Cipher Text: " + encryptedText)
print("Message through decryption: " + Decryption(encryptedText, key.upper()))

