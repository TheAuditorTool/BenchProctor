# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02895():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500
