# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24401():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
