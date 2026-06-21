# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest12637():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
