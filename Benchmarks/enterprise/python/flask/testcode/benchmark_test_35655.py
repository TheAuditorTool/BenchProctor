# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest35655():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
