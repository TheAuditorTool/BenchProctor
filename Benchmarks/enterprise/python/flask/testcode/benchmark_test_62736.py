# SPDX-License-Identifier: Apache-2.0
import hashlib
import base64
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest62736():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
