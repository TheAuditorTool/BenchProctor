# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest36148():
    ua_value = request.headers.get('User-Agent', '')
    data = relay_value(ua_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
