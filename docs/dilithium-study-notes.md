# CRYSTALS-Dilithium Study Notes

## Introduction

CRYSTALS-Dilithium is a lattice-based digital signature scheme selected by NIST as a post-quantum cryptography standard.

While CRYSTALS-Kyber focuses on key establishment, Dilithium provides authentication and integrity through digital signatures.

---

## Purpose of Digital Signatures

Digital signatures provide:

* Authentication
* Integrity
* Non-repudiation

A valid signature proves that a message was created by the holder of the private key and has not been modified.

---

## Security Foundation

Dilithium is based on:

* Module Learning With Errors (Module-LWE)
* Module Short Integer Solution (Module-SIS)

These problems are believed to remain difficult even for quantum computers.

---

## Core Mathematical Concepts

Dilithium relies on:

* Modular arithmetic
* Polynomial arithmetic
* Polynomial rings
* Number Theoretic Transform (NTT)
* Lattice-based cryptography

---

## High-Level Workflow

### Key Generation

Generate:

* Public matrix A
* Secret vectors
* Public verification key

Outputs:

* Public Key
* Secret Key

---

### Signing

Input:

* Message
* Secret Key

Output:

* Digital Signature

---

### Verification

Input:

* Message
* Signature
* Public Key

Output:

* Valid or Invalid

---

## Dilithium vs Kyber

Kyber:

* Key Encapsulation Mechanism (KEM)

Dilithium:

* Digital Signature Scheme

Both are based on lattice cryptography and were selected by NIST.

---

## Why Dilithium Matters

Future systems will require both:

* Quantum-resistant encryption
* Quantum-resistant signatures

Dilithium is one of the leading candidates for protecting digital signatures in a post-quantum world.

---

## Future Work

Planned topics:

* Module-SIS mathematics
* Signature generation details
* Verification algorithm
* Parameter sets
* Reference implementation analysis
