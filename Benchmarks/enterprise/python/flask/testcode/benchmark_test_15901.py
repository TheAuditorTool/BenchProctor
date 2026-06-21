# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15901():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    return jsonify({'error': 'An internal error occurred'}), 500
