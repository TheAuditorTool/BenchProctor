# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest21574():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if not auth_check('user', hashlib.sha256(str(graphql_var).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
