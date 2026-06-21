# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def relay_value(value):
    return value

def BenchmarkTest26938():
    host_value = request.headers.get('Host', '')
    data = relay_value(host_value)
    if str(data).lower() not in ('true', 'false'):
        return jsonify({'error': 'invalid boolean'}), 400
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
