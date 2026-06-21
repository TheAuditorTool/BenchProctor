# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest17440():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
