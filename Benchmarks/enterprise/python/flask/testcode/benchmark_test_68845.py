# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68845():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
