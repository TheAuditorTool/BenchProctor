# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12149():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
