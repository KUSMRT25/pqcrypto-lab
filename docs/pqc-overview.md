# Post-Quantum Cryptography (PQC) Overview

## Introduction

Post-Quantum Cryptography (PQC) refers to cryptographic algorithms that are designed to remain secure even against adversaries equipped with large-scale quantum computers.

Unlike classical cryptography, PQC aims to resist attacks from both classical and quantum computers.

The development of PQC has become increasingly important due to the potential impact of quantum algorithms such as Shor's Algorithm.

---

## Why Do We Need PQC?

Many widely used public-key cryptosystems rely on mathematical problems that are difficult for classical computers.

Examples include:

* RSA
* Diffie-Hellman
* Elliptic Curve Cryptography (ECC)

However, a sufficiently powerful quantum computer could break these systems efficiently using Shor's Algorithm.

As a result, the cybersecurity community is actively developing and standardizing quantum-resistant alternatives.

---

## NIST Standardization Project

The National Institute of Standards and Technology (NIST) launched the Post-Quantum Cryptography Standardization Project to identify and standardize secure quantum-resistant algorithms.

In recent years, NIST selected several algorithms for standardization, including:

### Key Encapsulation Mechanisms (KEM)

* CRYSTALS-Kyber

### Digital Signature Schemes

* CRYSTALS-Dilithium
* Falcon
* SPHINCS+

---

## Main Categories of PQC

### Lattice-Based Cryptography

Examples:

* CRYSTALS-Kyber
* CRYSTALS-Dilithium
* Falcon
* NTRU

Advantages:

* Strong security assumptions
* Efficient performance
* Practical implementations

---

### Hash-Based Cryptography

Examples:

* SPHINCS+

Advantages:

* Well-understood security
* Conservative design

---

### Code-Based Cryptography

Examples:

* Classic McEliece

Advantages:

* Long history of cryptanalysis
* Strong security record

---

### Multivariate Cryptography

Research area involving systems of multivariate polynomial equations.

Some candidates were studied during the NIST competition process.

---

## Goals of This Repository

This repository aims to:

* Study post-quantum cryptography
* Implement cryptographic algorithms
* Document learning progress
* Explore practical security considerations
* Provide educational resources

---

## Future Work

Planned topics include:

* CRYSTALS-Kyber
* CRYSTALS-Dilithium
* Falcon
* SPHINCS+
* Polynomial arithmetic
* Number Theoretic Transform (NTT)
* Lattice mathematics
* Benchmarking and testing

---

## References

* NIST Post-Quantum Cryptography Project
* CRYSTALS-Kyber Specification
* CRYSTALS-Dilithium Specification
* Open Quantum Safe (OQS)
