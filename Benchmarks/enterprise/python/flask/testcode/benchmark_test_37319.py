# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest37319():
    user_id = request.args.get('id', '')
    data = default_blank(user_id)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
