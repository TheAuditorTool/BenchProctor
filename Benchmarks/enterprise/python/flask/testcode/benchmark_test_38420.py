# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import ast
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest38420():
    xml_value = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
