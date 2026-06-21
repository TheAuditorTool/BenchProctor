# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68419():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
