# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest42918():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
