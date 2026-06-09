"""
Diffie-Hellman Key Exchange

Educational implementation.

Applications:
- TLS
- SSH
- VPNs
"""


def generate_public_key(g, private_key, p):
    return pow(g, private_key, p)


def generate_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)


if __name__ == "__main__":

    p = 23
    g = 5

    alice_private = 6
    bob_private = 15

    alice_public = generate_public_key(g, alice_private, p)
    bob_public = generate_public_key(g, bob_private, p)

    alice_secret = generate_shared_secret(
        bob_public,
        alice_private,
        p
    )

    bob_secret = generate_shared_secret(
        alice_public,
        bob_private,
        p
    )

    print("Alice Public Key:", alice_public)
    print("Bob Public Key:", bob_public)

    print("Alice Shared Secret:", alice_secret)
    print("Bob Shared Secret:", bob_secret)
