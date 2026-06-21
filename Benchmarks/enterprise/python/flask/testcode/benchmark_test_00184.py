# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00184():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
