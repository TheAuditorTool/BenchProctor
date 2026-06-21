# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest34522():
    auth_header = request.headers.get('Authorization', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(auth_header).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
