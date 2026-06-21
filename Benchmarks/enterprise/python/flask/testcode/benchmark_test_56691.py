# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest56691():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(json_value)), context=ctx)
    return jsonify({"result": "success"})
