# SPDX-License-Identifier: Apache-2.0
import hashlib
import base64
from flask import request, jsonify
import os


def BenchmarkTest01595():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
