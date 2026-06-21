# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36826():
    raw_body = request.get_data(as_text=True)
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
