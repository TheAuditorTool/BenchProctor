# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32002():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
