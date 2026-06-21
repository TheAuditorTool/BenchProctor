# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest73051():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data, _sep, _rest = str(yaml_value).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
