# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58117():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
