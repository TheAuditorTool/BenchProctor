# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31707():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
