# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49645():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
