# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest11354():
    cookie_value = request.cookies.get('session_token', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(cookie_value).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
