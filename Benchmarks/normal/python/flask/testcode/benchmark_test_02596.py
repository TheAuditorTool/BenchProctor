# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest02596():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
