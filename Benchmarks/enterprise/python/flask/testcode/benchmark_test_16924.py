# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16924():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    return jsonify({'error': 'An internal error occurred'}), 500
