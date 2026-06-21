# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10920():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
