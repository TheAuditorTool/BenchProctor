# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31319():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
