# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25126():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
