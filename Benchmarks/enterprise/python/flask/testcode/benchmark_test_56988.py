# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest56988():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
