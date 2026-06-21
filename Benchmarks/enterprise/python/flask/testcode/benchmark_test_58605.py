# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest58605():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
