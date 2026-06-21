# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08073():
    cookie_value = request.cookies.get('session_token', '')
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
