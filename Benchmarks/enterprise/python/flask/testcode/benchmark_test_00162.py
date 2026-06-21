# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest00162():
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
