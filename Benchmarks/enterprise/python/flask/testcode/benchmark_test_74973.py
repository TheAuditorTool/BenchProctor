# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74973():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
