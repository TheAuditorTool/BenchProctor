# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest21343():
    secret_value = 'feature_flag_value'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
