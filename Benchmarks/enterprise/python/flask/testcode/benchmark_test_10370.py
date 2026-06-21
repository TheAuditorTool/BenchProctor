# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10370():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
