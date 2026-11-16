from pwdlib import PasswordHash
ph = PasswordHash.recommended() 
h1 = ph.hash("qwerty123")
h2 = ph.hash("qwerty123")

print("Хеш 1:", h1)
print("Хеш 2:", h2)
print("Однакові?", h1 == h2) 
print("Правильний:", ph.verify("qwerty123", h1))  # True
print("Неправильний:", ph.verify("qwerty124", h1))  # False
print("Другий хеш теж підходить:", ph.verify("qwerty123", h2))  # True

parts = h1.split("$")
print("Алгоритм:", parts[1])
print("Параметри:", parts[3]) 
