import tkinter as tk

#Encrypts plaintext using the Vigenère cipher with the given key.
def vigenere_cipher(plaintext,key):
    ciphertext= ""
    key_len= len(key)
    for i, char in enumerate(plaintext):
        #plaintext-- error message will appear if it's not in all uppercase letters, no spaces
        if not char.isalpha() or not char.isupper():
            raise ValueError("The Plaintext must be in all uppercase letters wit no spaces only")
        if not key[i % key_len].isalpha() or not key[i % key_len].isupper():
            raise ValueError("The Key must be in all uppercase letters with no spaces only")
        #Calculates the shifting value
        shifting= ord(key[i % key_len]) - ord('A')  

        #The ciphertext produced by encrypting plaintext using the Vigenère cipher with the given key.
        cipher_char= chr((ord(char) - ord('A') + shifting)  % 26 + ord ('A'))
        ciphertext += cipher_char
#The loop continues to iterate over each character in the plaintext, generating a new ciphertext character for each one.
# Once the loop finished, final ciphertext string will be returned to the output of the function