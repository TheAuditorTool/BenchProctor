# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54106():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
