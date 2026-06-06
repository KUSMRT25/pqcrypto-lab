"""
Number Theoretic Transform (NTT)

Educational implementation of a basic NTT.

Applications:
- CRYSTALS-Kyber
- CRYSTALS-Dilithium
- Fast polynomial multiplication
"""


def mod_pow(base, exp, mod):
    result = 1

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod

        base = (base * base) % mod
        exp //= 2

    return result


def ntt(poly, root, q):
    """
    Forward NTT.

    Parameters:
        poly : polynomial coefficients
        root : primitive root of unity
        q    : modulus

    Returns:
        NTT(poly)
    """

    n = len(poly)
    result = [0] * n

    for k in range(n):

        value = 0

        for j in range(n):

            power = (j * k) % n

            value += poly[j] * mod_pow(root, power, q)

        result[k] = value % q

    return result


if __name__ == "__main__":

    q = 17
    root = 9

    poly = [1, 2, 3, 4]

    print("Input Polynomial:")
    print(poly)

    transformed = ntt(poly, root, q)

    print("NTT Result:")
    print(transformed)
