# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest17003():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
