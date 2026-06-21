# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest36694():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = relay_value(config_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
