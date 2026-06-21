# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest50907():
    header_value = request.headers.get('X-Custom-Header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
