# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05309():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
