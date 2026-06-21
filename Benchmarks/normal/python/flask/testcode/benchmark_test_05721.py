# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05721():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
