# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest19947():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
