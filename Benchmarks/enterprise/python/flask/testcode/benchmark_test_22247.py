# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest22247():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
