# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest61795():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
