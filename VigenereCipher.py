def encryption(message, key):
    encrypted_text = ''
    key_length = len(key)
    for i in range(len(message)):

        char = message[i]

        if char.isalpha():

            shift = ord(key[i % key_length].lower()) - ord('a')

            if char.isupper():

                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)

            elif char.islower():

                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
    return encrypted_text


def decryption(cipherText , key):
    decrypted_text = ''
    key_length = len(key)
    for i in range(len(cipherText)):
        char = cipherText[i]
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

message = input("Enter Message to be encrypted: ")
key = input("Enter key: ")
cipher_text = encryption(message, key)
decrypted_message = decryption(cipher_text , key)
print("Original Message: ", message)
print("Encrypted Message: ", cipher_text)
print("Decrypted Message: " , decrypted_message)

