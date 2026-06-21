# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest04042():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = bytes.fromhex(file_value).decode('utf-8', 'ignore')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
