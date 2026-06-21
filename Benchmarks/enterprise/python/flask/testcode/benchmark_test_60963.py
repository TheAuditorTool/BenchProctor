# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60963():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
