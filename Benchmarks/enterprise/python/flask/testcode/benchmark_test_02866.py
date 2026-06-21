# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest02866():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
