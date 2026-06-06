# CRYSTALS-Kyber Study Notes

## Introduction

CRYSTALS-Kyber is a lattice-based key encapsulation mechanism (KEM) selected by NIST as a post-quantum cryptography standard.

Kyber is designed to remain secure against both classical and quantum adversaries while maintaining efficient performance.

---

## Security Foundation

Kyber is based on the Module Learning With Errors (Module-LWE) problem.

The security assumption is believed to be resistant to attacks from quantum computers.

---

## Core Mathematical Concepts

Kyber relies on:

* Modular arithmetic
* Polynomial arithmetic
* Polynomial rings
* Number Theoretic Transform (NTT)
* Module-LWE

---

## High-Level Workflow

### Key Generation

Generate:

* Public parameter matrix A
* Secret vector s
* Error vector e

Compute:

t = A · s + e

Public Key:

(A, t)

Secret Key:

s

---

### Encapsulation

Generate a random secret and encrypt it using the public key.

Outputs:

* Ciphertext
* Shared Secret

---

### Decapsulation

Use the secret key to recover the shared secret from the ciphertext.

---

## Why Kyber Matters

Traditional public-key cryptography such as RSA and ECC may become vulnerable to large-scale quantum computers.

Kyber provides a practical alternative that is believed to remain secure in the post-quantum era.

---

## Future Work

Planned topics:

* Detailed Module-LWE explanation
* NTT optimization
* Kyber parameter sets
* Reference implementation analysis
* Benchmarking
