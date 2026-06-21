# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest42404():
    auth_header = request.headers.get('Authorization', '')
    requests.post('http://api.prod.internal/data', data=str(auth_header))
    return jsonify({"result": "success"})
