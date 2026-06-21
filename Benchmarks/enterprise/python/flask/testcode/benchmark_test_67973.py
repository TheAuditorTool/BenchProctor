# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest67973():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
