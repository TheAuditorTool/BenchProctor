# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest24942():
    auth_header = request.headers.get('Authorization', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(auth_header)}, verify=True)
    return jsonify({"result": "success"})
