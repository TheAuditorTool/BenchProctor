# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01360():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
