# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest19035():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = str(config_value).replace('\x00', '')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
