# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest62994():
    cookie_value = request.cookies.get('session_token', '')
    requests.post('https://api.prod.internal/data', data=str(cookie_value), verify=True)
    return jsonify({"result": "success"})
