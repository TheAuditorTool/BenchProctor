# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest27431():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = default_blank(yaml_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
