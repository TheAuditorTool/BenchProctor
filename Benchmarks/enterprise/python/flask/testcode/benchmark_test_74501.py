# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest74501():
    secret_value = 'config_secret_test_abc123'
    data = default_blank(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
