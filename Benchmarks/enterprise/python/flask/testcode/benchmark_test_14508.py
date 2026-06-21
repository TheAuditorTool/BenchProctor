# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest14508():
    header_value = request.headers.get('X-Custom-Header', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(header_value)).read()
    return jsonify({"result": "success"})
