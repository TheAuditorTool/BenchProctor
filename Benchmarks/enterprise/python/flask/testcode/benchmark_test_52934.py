# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import jsonify


def BenchmarkTest52934():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
