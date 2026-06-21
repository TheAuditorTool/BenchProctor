# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21646():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
