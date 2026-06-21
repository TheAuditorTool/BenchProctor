# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63699():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
