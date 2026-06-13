# Learning With Errors (LWE) Study Notes

## Introduction

Learning With Errors (LWE) is one of the most important mathematical problems in modern post-quantum cryptography.

Many lattice-based cryptographic systems derive their security from the assumed hardness of solving LWE instances.

Examples include:

* CRYSTALS-Kyber
* CRYSTALS-Dilithium
* FrodoKEM

---

## Basic Idea

Suppose we have:

* A secret vector s
* A random matrix A
* A small error vector e

We compute:

b = A·s + e

The public information is:

(A, b)

The challenge is to recover the secret vector s.

---

## Why Is It Difficult?

Without the error term:

b = A·s

The system can be solved efficiently using linear algebra.

With the error term:

b = A·s + e

the problem becomes significantly harder.

The noise hides the secret information.

---

## Security Intuition

The attacker observes:

(A, b)

but does not know:

* s
* e

Recovering s requires separating the hidden signal from random noise.

---

## Relationship to Lattice Cryptography

LWE can be reduced to certain worst-case lattice problems.

This connection provides strong theoretical security guarantees.

---

## Importance in PQC

LWE is considered one of the primary foundations of post-quantum cryptography because no efficient classical or quantum algorithms are known for solving appropriately parameterized instances.

---

## Future Topics

* Ring-LWE
* Module-LWE
* Kyber Security Foundations
* Dilithium Security Foundations
