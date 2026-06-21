# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest70432():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    requests.get(str(data))
    return jsonify({"result": "success"})
