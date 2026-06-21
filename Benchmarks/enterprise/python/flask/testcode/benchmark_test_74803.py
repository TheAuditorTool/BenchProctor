# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74803():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
