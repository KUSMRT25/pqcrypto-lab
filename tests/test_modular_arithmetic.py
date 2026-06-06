from implementations.modular_arithmetic.modular_arithmetic import *

def test_mod_add():
assert mod_add(10, 15, 7) == 4

def test_mod_sub():
assert mod_sub(10, 15, 7) == 2

def test_mod_mul():
assert mod_mul(10, 15, 7) == 3

def test_mod_pow():
assert mod_pow(10, 15, 7) == pow(10, 15, 7)
