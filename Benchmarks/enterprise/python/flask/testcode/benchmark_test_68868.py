# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68868():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
