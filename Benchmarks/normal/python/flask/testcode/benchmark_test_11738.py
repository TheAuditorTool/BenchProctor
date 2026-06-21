# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest11738():
    user_id = request.args.get('id', '')
    data = to_text(user_id)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
