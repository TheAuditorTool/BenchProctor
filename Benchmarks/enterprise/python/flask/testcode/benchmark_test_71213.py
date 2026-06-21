# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71213():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    return jsonify({'error': 'An internal error occurred'}), 500
