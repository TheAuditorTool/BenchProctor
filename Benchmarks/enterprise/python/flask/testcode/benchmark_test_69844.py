# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest69844():
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
