# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest51287():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = default_blank(forwarded_ip)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
