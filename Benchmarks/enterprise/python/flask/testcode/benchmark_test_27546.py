# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27546():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
