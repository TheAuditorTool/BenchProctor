# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest17470():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    request_state['last_input'] = file_value
    data = request_state['last_input']
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
