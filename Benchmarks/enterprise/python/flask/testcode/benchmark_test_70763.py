# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest70763():
    ua_value = request.headers.get('User-Agent', '')
    data = default_blank(ua_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
