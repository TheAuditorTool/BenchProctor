# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55842():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
