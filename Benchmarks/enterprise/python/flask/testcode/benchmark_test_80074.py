# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80074():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
