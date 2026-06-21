# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10053():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
