"""
Modular Arithmetic Library

This module provides basic modular arithmetic operations
commonly used in cryptography.
"""

def mod_add(a, b, n):
"""
Modular addition.

```
(a + b) mod n
"""
return (a + b) % n
```

def mod_sub(a, b, n):
"""
Modular subtraction.

```
(a - b) mod n
"""
return (a - b) % n
```

def mod_mul(a, b, n):
"""
Modular multiplication.

```
(a * b) mod n
"""
return (a * b) % n
```

def mod_pow(a, b, n):
"""
Modular exponentiation.

```
a^b mod n
"""
return pow(a, b, n)
```

if **name** == "**main**":
print("Modular Arithmetic Demo")
print("-----------------------")

```
print("mod_add(10, 15, 7) =", mod_add(10, 15, 7))
print("mod_sub(10, 15, 7) =", mod_sub(10, 15, 7))
print("mod_mul(10, 15, 7) =", mod_mul(10, 15, 7))
print("mod_pow(10, 15, 7) =", mod_pow(10, 15, 7))
```
