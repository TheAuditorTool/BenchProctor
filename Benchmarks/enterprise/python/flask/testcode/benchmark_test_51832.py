# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51832():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    return jsonify({'error': 'An internal error occurred'}), 500
