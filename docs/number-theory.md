# Number Theory Basics

## Introduction

Number theory is one of the most important mathematical foundations of modern cryptography.

Many cryptographic systems, including RSA, Diffie-Hellman, Elliptic Curve Cryptography (ECC), and Post-Quantum Cryptography (PQC), rely on concepts from number theory.

This document provides a brief introduction to the key ideas that will be used throughout this project.

---

## Prime Numbers

A prime number is a positive integer greater than 1 that has exactly two divisors:

* 1
* itself

Examples:

* 2
* 3
* 5
* 7
* 11
* 13

Prime numbers are essential for cryptographic algorithms such as RSA.

---

## Greatest Common Divisor (GCD)

The Greatest Common Divisor of two integers is the largest positive integer that divides both numbers.

Example:

gcd(12, 18) = 6

The Euclidean Algorithm is commonly used to compute GCD efficiently.

Applications:

* RSA
* Modular inverse computation
* Key generation

---

## Modular Arithmetic

Modular arithmetic studies arithmetic operations under a modulus.

Examples:

17 mod 5 = 2

because

17 = 3 × 5 + 2

Operations:

* Addition
* Subtraction
* Multiplication
* Exponentiation

Applications:

* RSA
* Diffie-Hellman
* Elliptic Curve Cryptography

---

## Modular Inverse

Given integers a and n,

a⁻¹ mod n

is called the modular inverse if

(a × a⁻¹) mod n = 1

The modular inverse is usually computed using the Extended Euclidean Algorithm.

Applications:

* RSA private key generation
* Elliptic Curve Cryptography

---

## Future Topics

This project will expand on:

* Euler's Totient Function
* Fermat's Little Theorem
* Chinese Remainder Theorem
* Miller-Rabin Primality Test
* RSA Mathematics
* Lattice Mathematics for PQC

---

## References

* Introduction to Modern Cryptography
* Handbook of Applied Cryptography
* NIST Post-Quantum Cryptography Project
