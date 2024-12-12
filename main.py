import random as r, string as s

elements = s.ascii_letters + s.ascii_lowercase + s.ascii_uppercase + s.punctuation + s.digits50

password = ""

longitud = int(input("¡Que tan laga sera la variable:"))
for in range(longitud):
    password += r.choice(elements)
print(password)