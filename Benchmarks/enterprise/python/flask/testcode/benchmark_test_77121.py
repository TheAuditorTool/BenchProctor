# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest77121():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    eval(str(data))
    return jsonify({"result": "success"})
