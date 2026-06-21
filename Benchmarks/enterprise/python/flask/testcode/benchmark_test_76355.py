# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest76355():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
