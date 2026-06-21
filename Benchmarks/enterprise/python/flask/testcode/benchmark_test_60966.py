# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60966():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    return jsonify({'error': 'An internal error occurred'}), 500
