# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest03049():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    prefix = ''
    data = prefix + str(file_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
