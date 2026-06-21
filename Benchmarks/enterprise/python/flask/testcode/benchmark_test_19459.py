# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest19459():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
