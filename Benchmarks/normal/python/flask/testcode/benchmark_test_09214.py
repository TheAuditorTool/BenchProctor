# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09214():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    return jsonify({'error': 'An internal error occurred'}), 500
