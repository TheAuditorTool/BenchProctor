# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest22170():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
