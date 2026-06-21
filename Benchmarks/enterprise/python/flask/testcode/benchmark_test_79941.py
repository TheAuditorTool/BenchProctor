# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79941():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    return jsonify({'error': 'An internal error occurred'}), 500
