# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09830():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
