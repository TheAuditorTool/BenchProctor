# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06221():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
