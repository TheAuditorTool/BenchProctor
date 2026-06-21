# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import re
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest06549():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    Fernet(processed.encode() if isinstance(processed, str) else processed).encrypt(b'data')
    return jsonify({"result": "success"})
