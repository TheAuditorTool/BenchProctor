# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14366():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
