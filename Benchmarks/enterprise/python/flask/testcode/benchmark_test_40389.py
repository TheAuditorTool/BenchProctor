# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40389():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
