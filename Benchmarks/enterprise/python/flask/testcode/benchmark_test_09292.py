# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest09292():
    secret_value = 'config_secret_test_abc123'
    Fernet(secret_value.encode() if isinstance(secret_value, str) else secret_value).encrypt(b'data')
    return jsonify({"result": "success"})
