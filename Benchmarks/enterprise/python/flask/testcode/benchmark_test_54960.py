# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest54960():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(prop_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
