def encrypt(message, s):
    result = ""
    for char in message:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char 
    return result

def decrypt(text, s):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char 
    return result

message = input("Enter message to be encrypted: ")
s = int(input('Enter shift value: '))
cipher_text = encrypt(message, s)
decrypted_text = decrypt(cipher_text, s)

print('Message:', message)
print('Encrypted Text:', cipher_text)
print('Decrypted Text:', decrypted_text)
