# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43739():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
