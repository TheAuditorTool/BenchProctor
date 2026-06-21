# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20349():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
