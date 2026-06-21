# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest70578():
    secret_value = 'config_secret_test_abc123'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
