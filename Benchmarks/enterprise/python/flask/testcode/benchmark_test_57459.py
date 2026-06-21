# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest57459():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    Fernet(prop_value.encode() if isinstance(prop_value, str) else prop_value).encrypt(b'data')
    return jsonify({"result": "success"})
