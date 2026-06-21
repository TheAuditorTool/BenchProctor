# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest18777():
    origin_value = request.headers.get('Origin', '')
    _resp = requests.get(str(origin_value))
    exec(_resp.text)
    return jsonify({"result": "success"})
