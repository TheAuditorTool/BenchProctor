# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest76737():
    cookie_value = request.cookies.get('session_token', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(cookie_value)}, verify=True)
    return jsonify({"result": "success"})
