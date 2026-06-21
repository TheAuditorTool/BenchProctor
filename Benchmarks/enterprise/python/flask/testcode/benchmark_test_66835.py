# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest66835():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    request_state['last_input'] = config_value
    data = request_state['last_input']
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return jsonify({"result": "success"})
