# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def ensure_str(value):
    return str(value)

def BenchmarkTest43995():
    host_value = request.headers.get('Host', '')
    data = ensure_str(host_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
