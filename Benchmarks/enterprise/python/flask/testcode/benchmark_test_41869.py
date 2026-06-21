# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41869():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
