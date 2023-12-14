import random
password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

long_contra = int(input("escribe la longitud de la contraseña"))

generada = ""


for i in range(long_contra):
    generada += random.choice(password)

print(generada)    
