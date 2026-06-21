# SPDX-License-Identifier: Apache-2.0
import hashlib
import base64
from flask import request, jsonify


def BenchmarkTest05326():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
