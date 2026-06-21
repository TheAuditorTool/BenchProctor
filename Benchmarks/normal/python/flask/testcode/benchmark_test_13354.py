# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13354():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    eval(str(data))
    return jsonify({"result": "success"})
