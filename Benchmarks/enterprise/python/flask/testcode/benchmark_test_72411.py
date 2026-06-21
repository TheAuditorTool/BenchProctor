# SPDX-License-Identifier: Apache-2.0
import requests
import base64
from flask import request, jsonify


def BenchmarkTest72411():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    requests.get(str(data))
    return jsonify({"result": "success"})
