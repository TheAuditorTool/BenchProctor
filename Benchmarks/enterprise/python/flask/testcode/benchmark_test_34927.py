# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest34927():
    secret_value = 'config_secret_test_abc123'
    parts = []
    for token in str(secret_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
