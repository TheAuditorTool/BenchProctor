# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32478():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
