# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10666():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    return jsonify({'error': 'An internal error occurred'}), 500
