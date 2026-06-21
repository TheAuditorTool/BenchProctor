# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import requests


def BenchmarkTest56001():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
