# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest00646():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    request_state['last_input'] = yaml_value
    data = request_state['last_input']
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
