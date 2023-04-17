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

#Creating GUI window with tkinter
window = tk.Tk()
window.geometry("500x400")
window.title("Vigenère Cipher")

#Allocating the font styles
title_font= ("Helvetica", 20, "bold")
input_font= ("Helvetica", 12)

#Title label
title_label = tk.Label(window, text="Vigenère Cipher", font=title_font)
title_label.pack(pady=10)

#Frame for the input fields
input_frame = tk.Frame(window)
input_frame.pack()

#Labels and entry fields for plaintext and key
plaintext_label = tk.Label(input_frame, text="Plaintext:", font=input_font)
plaintext_label.grid(row=0, column=0, padx=10, pady=10)
plaintext_entry = tk.Entry(input_frame, font=input_font)
plaintext_entry.grid(row=0, column=1, padx=10, pady=10)

key_label = tk.Label(input_frame, text="Key:", font=input_font)
key_label.grid(row=1, column=0, padx=10, pady=10)
key_entry = tk.Entry(input_frame, font=input_font)
key_entry.grid(row=1, column=1, padx=10, pady=10)

#Define a function for button clicks

#Button to encrypt the message

#Create a label for the output ciphertext

#Window background color and border

#Start the main event
