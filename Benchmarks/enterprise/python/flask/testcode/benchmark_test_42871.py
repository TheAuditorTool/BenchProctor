# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest42871():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    Fernet(config_value.encode() if isinstance(config_value, str) else config_value).encrypt(b'data')
    return jsonify({"result": "success"})
