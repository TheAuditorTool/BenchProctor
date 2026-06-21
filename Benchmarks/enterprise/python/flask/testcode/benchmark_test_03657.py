# SPDX-License-Identifier: Apache-2.0
import hashlib
import base64
from flask import request, jsonify
import os


def BenchmarkTest03657():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
