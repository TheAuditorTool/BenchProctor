# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import ast
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest61429():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
