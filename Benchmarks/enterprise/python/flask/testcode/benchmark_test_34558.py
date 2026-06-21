# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import urllib.request


def BenchmarkTest34558():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
