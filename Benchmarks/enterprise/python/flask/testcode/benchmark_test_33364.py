# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33364():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
