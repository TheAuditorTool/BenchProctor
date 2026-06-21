# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest13423():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
