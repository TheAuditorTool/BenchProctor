# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest03912():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = file_value.decode('utf-8', 'ignore') if isinstance(file_value, bytes) else file_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
