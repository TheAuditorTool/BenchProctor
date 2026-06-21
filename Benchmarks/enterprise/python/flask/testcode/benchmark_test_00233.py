# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00233():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
