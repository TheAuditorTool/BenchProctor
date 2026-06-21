# SPDX-License-Identifier: Apache-2.0
import hashlib
import base64
from flask import request, jsonify


def BenchmarkTest26645():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
