# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest08525():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
