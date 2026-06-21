# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest70621():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = (lambda v: v.strip())(yaml_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
