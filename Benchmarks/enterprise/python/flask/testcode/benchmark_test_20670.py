# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20670():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
