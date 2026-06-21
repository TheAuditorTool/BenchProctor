# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08096():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
