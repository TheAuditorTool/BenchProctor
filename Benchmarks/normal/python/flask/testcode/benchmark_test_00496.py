# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def relay_value(value):
    return value

def BenchmarkTest00496():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = relay_value(forwarded_ip)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
