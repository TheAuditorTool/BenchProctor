# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest07907():
    cookie_value = request.cookies.get('session_token', '')
    requests.post('http://api.prod.internal/data', data=str(cookie_value))
    return jsonify({"result": "success"})
