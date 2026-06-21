# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23756():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
