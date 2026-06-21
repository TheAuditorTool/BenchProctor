# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02711():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
