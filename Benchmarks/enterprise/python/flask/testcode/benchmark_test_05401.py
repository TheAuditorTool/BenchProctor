# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05401():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
