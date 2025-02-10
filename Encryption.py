import random
import string

characters = " " + string.punctuation + string.ascii_letters + string.digits 
characters = list(characters)
key = characters.copy()

random.shuffle(key)

#Encrypting the text
text = input("What is your private message? ")
encrypt_text = " "

for i in text:
    index = characters.index(i)
    encrypt_text += key[index]

print(f"Orignal messsage: {text}")
print(f"Encrypted messsage: {encrypt_text}")

#Decrypting the text
encrypt_text = input("Enter the encrypted message to reveal: ")
text = " "

for i in encrypt_text:
    index = key.index(i)
    text += characters[index]

print(f"Encrypted messsage: {encrypt_text}")
print(f"Orignal messsage: {text}")
