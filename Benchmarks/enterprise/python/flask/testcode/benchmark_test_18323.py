# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest18323():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    parts = str(yaml_value).split(',')
    data = ','.join(parts)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
