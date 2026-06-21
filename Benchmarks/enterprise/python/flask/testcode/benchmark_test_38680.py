# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import json


def BenchmarkTest38680():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
