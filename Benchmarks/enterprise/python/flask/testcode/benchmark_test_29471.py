# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest29471():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
