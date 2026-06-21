# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09188():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
