# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30402():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
