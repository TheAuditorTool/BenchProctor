# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49759():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
