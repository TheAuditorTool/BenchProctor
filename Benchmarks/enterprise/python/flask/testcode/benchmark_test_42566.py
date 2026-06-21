# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest42566():
    referer_value = request.headers.get('Referer', '')
    requests.post('http://api.prod.internal/data', data=str(referer_value))
    return jsonify({"result": "success"})
