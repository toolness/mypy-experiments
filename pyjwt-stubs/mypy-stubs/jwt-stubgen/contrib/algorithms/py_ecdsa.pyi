# Stubs for jwt.contrib.algorithms.py_ecdsa (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from jwt.algorithms import Algorithm

class ECAlgorithm(Algorithm):
    SHA256 = ...  # type: Any
    SHA384 = ...  # type: Any
    SHA512 = ...  # type: Any
    hash_alg = ...  # type: Any
    def __init__(self, hash_alg) -> None: ...
    def prepare_key(self, key): ...
    def sign(self, msg, key): ...
    def verify(self, msg, key, sig): ...
