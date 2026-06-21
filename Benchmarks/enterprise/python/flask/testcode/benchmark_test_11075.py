# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest11075():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
