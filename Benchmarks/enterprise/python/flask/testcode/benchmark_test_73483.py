# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest73483():
    header_value = request.headers.get('X-Custom-Header', '')
    requests.post('https://api.prod.internal/data', data=str(header_value), verify=True)
    return jsonify({"result": "success"})
