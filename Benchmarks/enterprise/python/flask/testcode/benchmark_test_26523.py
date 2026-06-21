# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest26523():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
