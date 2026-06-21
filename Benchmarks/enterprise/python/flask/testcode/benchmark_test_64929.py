# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64929():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
