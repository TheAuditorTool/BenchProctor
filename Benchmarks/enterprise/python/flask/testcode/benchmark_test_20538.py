# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest20538():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = (lambda v: v.strip())(forwarded_ip)
    requests.get(str(data))
    return jsonify({"result": "success"})
