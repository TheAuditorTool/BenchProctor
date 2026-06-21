# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import request, jsonify
import ast
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest24848():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
