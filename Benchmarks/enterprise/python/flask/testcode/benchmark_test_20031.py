# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20031():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
