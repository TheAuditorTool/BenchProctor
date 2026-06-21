# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest40806():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
