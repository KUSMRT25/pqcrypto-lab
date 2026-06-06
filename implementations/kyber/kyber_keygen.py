"""
Simplified Kyber Key Generation

Educational demonstration only.

Not a real CRYSTALS-Kyber implementation.
"""

import random

Q = 17
N = 4

def random_poly():
return [random.randint(0, Q - 1) for _ in range(N)]

def poly_add(a, b):
return [(a[i] + b[i]) % Q for i in range(N)]

def poly_mul(a, b):

```
result = [0] * (2 * N - 1)

for i in range(N):
    for j in range(N):
        result[i + j] += a[i] * b[j]

for k in range(N, len(result)):
    result[k - N] -= result[k]

return [x % Q for x in result[:N]]
```

def keygen():

```
A = random_poly()

s = random_poly()

e = random_poly()

t = poly_add(poly_mul(A, s), e)

return (A, t), s
```

if **name** == "**main**":

```
public_key, secret_key = keygen()

print("Public Key:")
print(public_key)

print()

print("Secret Key:")
print(secret_key)
```
