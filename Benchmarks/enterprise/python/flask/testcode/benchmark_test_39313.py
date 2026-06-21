# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39313():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500
