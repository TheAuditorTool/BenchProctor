# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest37489():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
