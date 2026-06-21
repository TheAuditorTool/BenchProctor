# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27453():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return jsonify({'error': 'An internal error occurred'}), 500
