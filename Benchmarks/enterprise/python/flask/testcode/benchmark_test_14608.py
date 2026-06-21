# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest14608():
    user_id = request.args.get('id', '')
    data = relay_value(user_id)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
