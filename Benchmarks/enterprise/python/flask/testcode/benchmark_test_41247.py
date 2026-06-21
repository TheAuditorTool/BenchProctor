# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41247():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
