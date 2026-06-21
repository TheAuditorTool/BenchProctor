# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest72191():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
