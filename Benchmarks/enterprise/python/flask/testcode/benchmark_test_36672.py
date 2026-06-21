# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest36672():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
