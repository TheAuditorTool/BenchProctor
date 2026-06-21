# SPDX-License-Identifier: Apache-2.0
import jwt
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest64996():
    secret_value = 'config_secret_test_abc123'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    processed = data[:64]
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return jsonify({"result": "success"})
