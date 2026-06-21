# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest77069():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    Fernet(secret_value.encode() if isinstance(secret_value, str) else secret_value).encrypt(b'data')
    return jsonify({"result": "success"})
