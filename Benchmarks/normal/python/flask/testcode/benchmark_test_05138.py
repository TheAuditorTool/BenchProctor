# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05138():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
