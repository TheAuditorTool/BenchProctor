# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest78705():
    ua_value = request.headers.get('User-Agent', '')
    digest = hashlib.sha256(('static_salt_123' + str(ua_value)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
