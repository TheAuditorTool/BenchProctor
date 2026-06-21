# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07639():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
