"""
Extended Euclidean Algorithm

Used for:

* GCD computation
* Bézout coefficients
* Modular inverse
* RSA key generation
  """

def gcd(a, b):
while b != 0:
a, b = b, a % b
return a

def extended_gcd(a, b):
if b == 0:
return a, 1, 0

```
gcd_value, x1, y1 = extended_gcd(b, a % b)

x = y1
y = x1 - (a // b) * y1

return gcd_value, x, y
```

def mod_inverse(a, n):
gcd_value, x, y = extended_gcd(a, n)

```
if gcd_value != 1:
    raise ValueError("Modular inverse does not exist")

return x % n
```

if **name** == "**main**":
print("GCD(48,18) =", gcd(48, 18))

```
g, x, y = extended_gcd(48, 18)

print("Extended GCD:")
print("gcd =", g)
print("x =", x)
print("y =", y)

print("Modular Inverse")
print("3^-1 mod 11 =", mod_inverse(3, 11))
```
