"""
Miller-Rabin Primality Test

Probabilistic primality testing algorithm commonly used
for cryptographic prime generation.

Applications:

* RSA key generation
* Prime generation
* Cryptographic protocols
  """

import random

def miller_rabin(n, k=10):
"""
Miller-Rabin primality test.

```
Parameters:
    n : integer to test
    k : number of testing rounds

Returns:
    True  -> probably prime
    False -> composite
"""

if n == 2 or n == 3:
    return True

if n <= 1 or n % 2 == 0:
    return False

# Write n - 1 as d * 2^r
r = 0
d = n - 1

while d % 2 == 0:
    r += 1
    d //= 2

for _ in range(k):

    a = random.randrange(2, n - 1)

    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        continue

    for _ in range(r - 1):

        x = pow(x, 2, n)

        if x == n - 1:
            break

    else:
        return False

return True
```

if **name** == "**main**":

```
test_numbers = [
    17,
    19,
    23,
    25,
    91,
    101,
    7919
]

for num in test_numbers:

    if miller_rabin(num):
        print(f"{num} is probably prime")
    else:
        print(f"{num} is composite")
```
