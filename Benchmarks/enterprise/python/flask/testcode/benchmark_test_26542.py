# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest26542():
    referer_value = request.headers.get('Referer', '')
    if not auth_check('user', hashlib.sha256(str(referer_value).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
