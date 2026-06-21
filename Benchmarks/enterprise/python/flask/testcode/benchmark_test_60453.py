# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60453():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
