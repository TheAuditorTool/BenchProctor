# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54740():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
