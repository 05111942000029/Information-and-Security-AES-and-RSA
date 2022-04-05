from cryptography.fernet import Fernet

import time
start_time = time.time()

key = Fernet.generate_key() #Buat generate key step 1

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

with open('mykey.key', 'rb') as mykey: #baca key yang dibuat step 2
    key = mykey.read()

print(key)

f = Fernet(key) #Encrypt file yg ada step 3

with open('fitness.txt', 'rb') as original_file:
     original = original_file.read()

encrypted = f.encrypt(original)

with open('enc_fitness.txt', 'wb') as encrypyted_file:
     encrypyted_file.write(encrypted)

f = Fernet(key) #Decrypt encrypted file yg ada step 4

with open('enc_fitness.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_fitness.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

print("Process finished --- %s seconds ---" % (time.time() - start_time))