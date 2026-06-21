# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38900():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    eval(str(data))
    return jsonify({"result": "success"})
