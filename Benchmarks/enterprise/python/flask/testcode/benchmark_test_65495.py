# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest65495():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
