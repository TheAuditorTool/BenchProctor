# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import urllib.request


def BenchmarkTest29957():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
