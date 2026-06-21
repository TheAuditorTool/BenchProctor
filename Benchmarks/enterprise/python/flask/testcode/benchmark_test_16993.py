# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16993():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
