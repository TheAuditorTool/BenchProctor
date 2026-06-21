# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest49132():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(graphql_var)), context=ctx)
    return jsonify({"result": "success"})
