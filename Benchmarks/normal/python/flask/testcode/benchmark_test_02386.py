# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def relay_value(value):
    return value

def BenchmarkTest02386():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = relay_value(forwarded_ip)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
