# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01173():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
