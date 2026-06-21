# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest63626():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
