# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28389():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    exec(str(data))
    return jsonify({"result": "success"})
