# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04507():
    user_id = request.args.get('id', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(user_id)}
