# pqcrypto-lab

> Open-source implementations and educational resources for post-quantum cryptography.

---

## Mission

The emergence of large-scale quantum computing poses a significant challenge to traditional public-key cryptography. Algorithms such as RSA and Elliptic Curve Cryptography (ECC) may become vulnerable to quantum attacks, creating an urgent need for quantum-resistant cryptographic systems.

**pqcrypto-lab** is an open-source initiative focused on studying, implementing, documenting, and benchmarking post-quantum cryptographic algorithms. The project aims to make modern cryptography more accessible to students, researchers, and developers through transparent implementations and comprehensive educational resources.

---

## Goals

### Educational Goals

* Provide clear explanations of cryptographic concepts
* Build practical implementations from scratch
* Create learning resources for students and beginners
* Bridge the gap between theory and implementation

### Research Goals

* Explore NIST-standardized post-quantum algorithms
* Study performance and security trade-offs
* Analyze implementation challenges
* Develop benchmarking and testing frameworks

### Community Goals

* Encourage collaboration among cryptography enthusiasts
* Maintain open documentation and discussion
* Welcome contributions from students and researchers

---

## Project Scope

This repository covers both classical and post-quantum cryptography.

### Classical Cryptography

* Caesar Cipher
* Vigenère Cipher
* DES
* AES
* RSA
* Diffie-Hellman Key Exchange
* Elliptic Curve Cryptography (ECC)

### Post-Quantum Cryptography

#### Lattice-Based Cryptography

* CRYSTALS-Kyber
* CRYSTALS-Dilithium
* Falcon
* NTRU

#### Hash-Based Cryptography

* SPHINCS+

#### Code-Based Cryptography

* Classic McEliece

#### Additional Research Areas

* Quantum-resistant key exchange
* Digital signatures
* Hybrid cryptographic systems
* Secure implementation techniques

---

## Repository Structure

```text
pqcrypto-lab/
│
├── docs/
│   ├── cryptography-notes/
│   ├── pqc-guides/
│   └── research-summaries/
│
├── implementations/
│   ├── rsa/
│   ├── ecc/
│   ├── kyber/
│   ├── dilithium/
│   └── sphincs-plus/
│
├── experiments/
│   ├── benchmarks/
│   └── performance-tests/
│
├── examples/
│   ├── key-exchange/
│   ├── signatures/
│   └── hybrid-systems/
│
├── tests/
│
└── resources/
```

---

## Roadmap

### Foundation Phase

* [ ] Repository initialization
* [ ] Documentation framework
* [ ] Number theory review
* [ ] Modular arithmetic library
* [ ] Extended Euclidean Algorithm
* [ ] Fast modular exponentiation
* [ ] Miller-Rabin primality test

### Classical Cryptography Phase

* [ ] RSA implementation
* [ ] Diffie-Hellman implementation
* [ ] ECC implementation
* [ ] Cryptographic utility library

### Post-Quantum Cryptography Phase

* [ ] CRYSTALS-Kyber implementation study
* [ ] CRYSTALS-Dilithium implementation study
* [ ] Test vector validation
* [ ] Benchmark framework

### Advanced Phase

* [ ] Falcon implementation study
* [ ] SPHINCS+ implementation study
* [ ] Security analysis reports
* [ ] Interactive educational tools

---

## Technologies

* C
* Python
* Git
* OpenSSL
* SageMath

---

## Target Audience

This project is intended for:

* Students studying cryptography
* Cybersecurity researchers
* Open-source contributors
* Software engineers interested in secure systems
* Post-quantum cryptography enthusiasts

---

## Contribution Guide

Contributions are welcome.

Possible contribution areas include:

* Algorithm implementations
* Documentation improvements
* Security reviews
* Benchmarking and testing
* Educational materials
* Bug fixes and optimizations

If you would like to contribute, please open an issue before submitting major changes.

---

## Project Principles

1. Transparency over complexity
2. Education before optimization
3. Reproducible research
4. Open collaboration
5. Secure coding practices

---

## References

### NIST Post-Quantum Cryptography

https://csrc.nist.gov/projects/post-quantum-cryptography

### Open Quantum Safe

https://openquantumsafe.org

### PQClean

https://github.com/PQClean/PQClean

### CRYSTALS-Kyber

https://pq-crystals.org/kyber

### CRYSTALS-Dilithium

https://pq-crystals.org/dilithium

---

## Disclaimer

This repository is intended for educational and research purposes.

Cryptographic code contained in this repository should not be used in production environments without comprehensive security review, testing, and validation.

---

## License

Distributed under the MIT License.

See `LICENSE` for more information.

---

## Maintainer

**Baek Minjun**

Student Researcher | Cryptography Enthusiast

Interested in Post-Quantum Cryptography, Secure Systems, and Applied Cryptography.

---

*"Building practical understanding of the future of cryptography."*

## Current Progress

Implemented Components

* Modular Arithmetic
* Extended Euclidean Algorithm
* Miller-Rabin Primality Test
* RSA (Educational)
* Polynomial Arithmetic
* Number Theoretic Transform (NTT)
* Polynomial Ring Arithmetic
* Simplified Kyber Demonstration

Documentation

* Number Theory Notes
* Post-Quantum Cryptography Overview
* CRYSTALS-Kyber Study Notes
* CRYSTALS-Dilithium Study Notes
* Project Roadmap

Testing

* Modular Arithmetic Unit Tests
