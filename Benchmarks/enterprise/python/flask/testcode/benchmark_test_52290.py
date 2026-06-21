# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest52290():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
