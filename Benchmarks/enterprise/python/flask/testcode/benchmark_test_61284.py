# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61284():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
