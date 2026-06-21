# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest31489():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
