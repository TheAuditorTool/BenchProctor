# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest01063():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
