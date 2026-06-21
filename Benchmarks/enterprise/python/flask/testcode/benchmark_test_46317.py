# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46317():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    int(str(data))
    return jsonify({"result": "success"})
