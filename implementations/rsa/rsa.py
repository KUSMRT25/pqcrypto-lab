"""
Educational RSA Implementation

Features:

* Key Generation
* Encryption
* Decryption

For educational purposes only.
"""

from math import gcd

def mod_inverse(e, phi):
for d in range(2, phi):
if (e * d) % phi == 1:
return d
return None

def generate_keys():
p = 61
q = 53

```
n = p * q
phi = (p - 1) * (q - 1)

e = 17

while gcd(e, phi) != 1:
    e += 2

d = mod_inverse(e, phi)

return (e, n), (d, n)
```

def encrypt(message, public_key):
e, n = public_key
return pow(message, e, n)

def decrypt(ciphertext, private_key):
d, n = private_key
return pow(ciphertext, d, n)

if **name** == "**main**":

```
public_key, private_key = generate_keys()

message = 42

ciphertext = encrypt(message, public_key)

plaintext = decrypt(ciphertext, private_key)

print("Original Message:", message)
print("Ciphertext:", ciphertext)
print("Decrypted Message:", plaintext)
```
