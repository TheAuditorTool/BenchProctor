# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38200():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
