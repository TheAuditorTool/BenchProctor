# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest09381():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
