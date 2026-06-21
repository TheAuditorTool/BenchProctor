# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11171():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
