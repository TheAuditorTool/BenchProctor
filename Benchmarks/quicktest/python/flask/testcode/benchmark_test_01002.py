# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest01002():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
