# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest32363():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    requests.post('https://api.prod.internal/data', data=str(forwarded_ip), verify=True)
    return jsonify({"result": "success"})
