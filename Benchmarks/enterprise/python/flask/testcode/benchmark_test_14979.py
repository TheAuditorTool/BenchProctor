# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14979():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    return jsonify({'error': 'An internal error occurred'}), 500
