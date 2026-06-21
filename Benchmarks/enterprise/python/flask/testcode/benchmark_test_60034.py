# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest60034():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
