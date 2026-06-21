# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78100():
    auth_header = request.headers.get('Authorization', '')
    if auth_header not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = auth_header
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
