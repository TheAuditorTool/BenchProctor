# SPDX-License-Identifier: Apache-2.0
import jwt
import re
from flask import jsonify


def BenchmarkTest25371():
    secret_value = 'config_secret_test_abc123'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return jsonify({"result": "success"})
