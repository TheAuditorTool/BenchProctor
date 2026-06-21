# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest43682():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    Fernet(file_value.encode() if isinstance(file_value, str) else file_value).encrypt(b'data')
    return jsonify({"result": "success"})
