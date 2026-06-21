# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest59733():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
