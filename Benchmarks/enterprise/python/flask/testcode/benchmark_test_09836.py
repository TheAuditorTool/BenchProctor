# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest09836():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = to_text(file_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
