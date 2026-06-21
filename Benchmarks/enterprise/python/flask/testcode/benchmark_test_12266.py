# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest12266():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
