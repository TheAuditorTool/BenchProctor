# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45699():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
