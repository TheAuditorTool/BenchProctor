# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def relay_value(value):
    return value

def BenchmarkTest14464():
    header_value = request.headers.get('X-Custom-Header', '')
    data = relay_value(header_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
