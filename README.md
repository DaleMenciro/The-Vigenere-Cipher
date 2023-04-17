
# Laboratory Exercise 1

## Problem 3: The Vigenère Cipher
About: Your key is a keyword, which you then translate into corresponding letter values **0 – 25**. Then, to encrypt, write your message on one row (letters 0 – 25), and repeatedly write the keyword below it, adding each column, taking the result **mod 26**. These resultant numbers are the ciphertext. 

### How does it work?
- The **Autokey Method** makes use of the **Vigenere Cipher** table to encrypt and decrypt the plaintext. In this method, the priming key is just one letter.
- The first step in the autokey method is to decide on a priming key. Both sender and receiver have to agree on this key. The priming key is the single alphabet that is added to the beginning of messages to help make the key. The sender encrypts the message starting with writing the first letter of the plaintext on one line and the priming key under it. The rest of the plaintext is written as is, shifted one place to the right.



### Example
**Plaintext** - I	N	T	E	L	L	I	P	A	A	T

**Key** - R	I	N	T	E	L	L	I	P	A	A

----------------
**Ciphertext** - Z	V	G	X	P	W	T	X	P	A	T


## Module Requirements:
### Click the name for install instructions

 - [tkinter](https://docs.python.org/3/library/tkinter.html)
