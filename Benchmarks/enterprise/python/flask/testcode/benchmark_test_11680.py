# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11680():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
