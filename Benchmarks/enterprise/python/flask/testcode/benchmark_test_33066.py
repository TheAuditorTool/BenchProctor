# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33066():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
