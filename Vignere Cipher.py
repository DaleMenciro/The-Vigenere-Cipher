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
    return ciphertext

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
def encrypt_message():
    plaintext = plaintext_entry.get()
    key = key_entry.get()
     # Encrypt the plaintext using the Vigenère cipher with the key
    try:
        ciphertext = vigenere_cipher(plaintext, key)
        output_label.config(text="Ciphertext: " + ciphertext, fg="green")
    except ValueError as e:
        output_label.config(text="Error: " + str(e), fg="red")

#Button to encrypt the message
encrypt_button = tk.Button(window, text="Encrypt", font=input_font, command=encrypt_message)
encrypt_button.pack(pady=10)

#Create a label for the output ciphertext
output_label = tk.Label(window, font=input_font)
output_label.pack(pady=10)

# Create an exit button
exit_button = tk.Button(window, text="Exit", font=input_font, command=window.quit)
exit_button.pack(pady=10)

#Window background color and border
window.configure(bg="lightblue")
window.attributes("-alpha", 0.9)
window.overrideredirect(True)
window.overrideredirect(False)
window.attributes("-fullscreen", True)
window.attributes("-topmost", True)

#Start the main event
window.mainloop()