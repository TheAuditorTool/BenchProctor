# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16098():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
