# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest13335():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
