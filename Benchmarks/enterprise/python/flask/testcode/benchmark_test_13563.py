# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13563():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500
