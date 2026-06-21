# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32079():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
