# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest07557():
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
