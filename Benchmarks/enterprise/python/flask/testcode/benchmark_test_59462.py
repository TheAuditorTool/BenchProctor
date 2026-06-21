# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59462():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    return jsonify({'error': 'An internal error occurred'}), 500
