# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62713():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
