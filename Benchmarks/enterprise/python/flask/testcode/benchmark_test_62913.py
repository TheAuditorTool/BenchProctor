# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62913():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    return jsonify({'error': 'An internal error occurred'}), 500
