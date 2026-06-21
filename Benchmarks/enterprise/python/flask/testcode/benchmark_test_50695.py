# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest50695():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if not auth_check('user', hashlib.sha256(str(forwarded_ip).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
