# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest14056():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
