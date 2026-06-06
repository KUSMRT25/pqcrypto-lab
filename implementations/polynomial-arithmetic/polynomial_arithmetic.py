"""
Polynomial Arithmetic

Basic polynomial operations used in lattice-based cryptography.

Applications:

* CRYSTALS-Kyber
* CRYSTALS-Dilithium
* NTRU
  """

def poly_add(a, b):
n = max(len(a), len(b))
result = [0] * n

```
for i in range(n):
    ai = a[i] if i < len(a) else 0
    bi = b[i] if i < len(b) else 0
    result[i] = ai + bi

return result
```

def poly_sub(a, b):
n = max(len(a), len(b))
result = [0] * n

```
for i in range(n):
    ai = a[i] if i < len(a) else 0
    bi = b[i] if i < len(b) else 0
    result[i] = ai - bi

return result
```

def poly_mul(a, b):
result = [0] * (len(a) + len(b) - 1)

```
for i in range(len(a)):
    for j in range(len(b)):
        result[i + j] += a[i] * b[j]

return result
```

def poly_mod(poly, q):
return [x % q for x in poly]

if **name** == "**main**":

```
A = [1, 2, 3]
B = [4, 5]

print("A =", A)
print("B =", B)

print("Addition:")
print(poly_add(A, B))

print("Subtraction:")
print(poly_sub(A, B))

print("Multiplication:")
print(poly_mul(A, B))

print("Modulo 7:")
print(poly_mod(poly_mul(A, B), 7))
```
