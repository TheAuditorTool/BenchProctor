# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest29645():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
