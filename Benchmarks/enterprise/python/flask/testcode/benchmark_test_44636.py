# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def to_text(value):
    return str(value).strip()

def BenchmarkTest44636():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = to_text(json_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
