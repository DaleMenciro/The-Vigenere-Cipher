#Encrypts plaintext using the Vigenère cipher with the given key.
def vigenere_cipher(plaintext,key):
    ciphertext= ""
    key_len= len(key)
    for i, char in enumerate(plaintext):
#plaintext-- error message will appear if it's not in all uppercase letters, no spaces
#The ciphertext produced by encrypting plaintext using the Vigenère cipher with the given key.
