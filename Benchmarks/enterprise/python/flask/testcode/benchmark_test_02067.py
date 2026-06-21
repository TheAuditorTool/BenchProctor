# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02067():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
