# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest03597(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(processed).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
