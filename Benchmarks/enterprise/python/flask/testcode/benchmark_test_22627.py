# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest22627():
    header_value = request.headers.get('X-Custom-Header', '')
    _resp = requests.get(str(header_value))
    exec(_resp.text)
    return jsonify({"result": "success"})
