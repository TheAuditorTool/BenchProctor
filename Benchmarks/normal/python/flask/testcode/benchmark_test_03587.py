# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03587():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
