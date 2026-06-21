# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39608():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
