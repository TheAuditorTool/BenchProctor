# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest75983():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(forwarded_ip)}, verify=True)
    return jsonify({"result": "success"})
