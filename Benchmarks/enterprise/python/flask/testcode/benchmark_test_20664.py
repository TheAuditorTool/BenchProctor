# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20664():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
