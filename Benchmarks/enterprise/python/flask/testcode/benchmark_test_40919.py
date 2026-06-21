# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest40919():
    host_value = request.headers.get('Host', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(host_value)).read()
    return jsonify({"result": "success"})
