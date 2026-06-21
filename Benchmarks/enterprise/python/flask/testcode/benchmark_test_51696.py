# SPDX-License-Identifier: Apache-2.0
import secrets
import base64
from flask import request, jsonify


def BenchmarkTest51696():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
