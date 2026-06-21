# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest01887():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = file_value if file_value else 'default'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
