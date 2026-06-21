# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77888():
    auth_header = request.headers.get('Authorization', '')
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
