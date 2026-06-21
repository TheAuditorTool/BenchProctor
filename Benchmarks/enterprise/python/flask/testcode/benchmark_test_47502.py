# SPDX-License-Identifier: Apache-2.0
import hashlib
import base64
from flask import request, jsonify


def BenchmarkTest47502():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
