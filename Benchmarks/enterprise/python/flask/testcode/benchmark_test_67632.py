# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import json


def BenchmarkTest67632():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
