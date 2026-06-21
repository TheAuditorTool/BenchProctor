# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest04678():
    auth_header = request.headers.get('Authorization', '')
    data = relay_value(auth_header)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
