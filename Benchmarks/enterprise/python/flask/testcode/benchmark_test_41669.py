# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest41669():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data, _sep, _rest = str(prop_value).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
