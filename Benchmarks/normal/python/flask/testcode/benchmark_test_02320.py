# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest02320():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
