# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest66263():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
