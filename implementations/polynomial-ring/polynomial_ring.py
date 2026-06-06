"""
Polynomial Ring Arithmetic

Educational implementation of arithmetic in

Zq[x] / (x^n + 1)

Applications:

* CRYSTALS-Kyber
* CRYSTALS-Dilithium
  """

Q = 17
N = 4

def ring_add(a, b):
return [(a[i] + b[i]) % Q for i in range(N)]

def ring_sub(a, b):
return [(a[i] - b[i]) % Q for i in range(N)]

def ring_mul(a, b):
result = [0] * (2 * N - 1)

```
for i in range(N):
    for j in range(N):
        result[i + j] += a[i] * b[j]

for k in range(N, len(result)):
    result[k - N] -= result[k]

return [x % Q for x in result[:N]]
```

if **name** == "**main**":

```
A = [1, 2, 3, 4]
B = [4, 3, 2, 1]

print("A =", A)
print("B =", B)

print("A + B =", ring_add(A, B))
print("A - B =", ring_sub(A, B))
print("A * B =", ring_mul(A, B))
```
