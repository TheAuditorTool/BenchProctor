# SPDX-License-Identifier: Apache-2.0
import secrets
import base64
from flask import request, jsonify


def BenchmarkTest04934():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
