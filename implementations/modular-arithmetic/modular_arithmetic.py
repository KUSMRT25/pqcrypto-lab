def mod_add(a, b, n):
    return (a + b) % n

def mod_sub(a, b, n):
    return (a - b) % n

def mod_mul(a, b, n):
    return (a * b) % n

def mod_pow(a, b, n):
    return pow(a, b, n)


if __name__ == "__main__":
    print(mod_add(10, 15, 7))
    print(mod_sub(10, 15, 7))
    print(mod_mul(10, 15, 7))
    print(mod_pow(10, 15, 7))
