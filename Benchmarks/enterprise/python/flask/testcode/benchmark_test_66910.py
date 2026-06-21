# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66910():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    return jsonify({'error': 'An internal error occurred'}), 500
