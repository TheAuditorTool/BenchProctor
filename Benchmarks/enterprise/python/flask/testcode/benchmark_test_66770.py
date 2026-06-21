# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest66770():
    origin_value = request.headers.get('Origin', '')
    if not auth_check('user', hashlib.sha256(str(origin_value).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
